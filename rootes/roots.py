import json
from flask import Flask, render_template, request, redirect
from app import app
from models import *
from helpers.helps import *


def read():
    with open('database/user.json', 'r') as f:
        g = f.read()
        data = json.loads(g)
        f.close()
    return data


def read_for_car():
    with open('database/cars.json', 'r') as f:
        g = f.read()
        data = json.loads(g)
        f.close()
    return data


@app.route('/menu', methods=['Get'])
def general():
    us = User.query.all()
    return convert_all(us)


@app.route('/showCars', methods=['get'])
def show_car():
    cars = Cars.query.all()
    return convert_all(cars)


@app.route('/search', methods=['Get'])
def search_email():
    return render_template("search.html")


@app.route('/result/search', methods=['post'])
def result_search():
    form = request.form
    # d = read()
    # i = 0
    # h = d[0]
    # for k in d:
    #     if str(k['Email']) == form['email']:
    #         h = k
    #         i = i + 1
    # if i > 0:
    #     return h
    # elif i == 0:
    #     return "incorrect data"
    d = User.query.filter_by(email=form['email']).first()
    if User.query.filter_by(email=form['email']).first():
        return d.serialize
    else:
        return "<h1>incorrect data</h1>"


@app.route('/change', methods=['GET'])
def change():
    return render_template('change.html')


@app.route('/after_change', methods=['post'])
def after_change():
    form = request.form
    # dictionary = {
    #     "first_name": form['fname'],
    #     "last_name": form['lname'],
    #     "Email": form['email'],
    #     "id": form['id'],
    # }
    # d = read()
    # h = d[0]
    # i = 0
    # for k in d:
    #     if str(k['id']) == form['id']:
    #         h = k
    # for k in range(0, len(d)):
    #     if h == d[k]:
    #         i = k
    # d[i] = dictionary
    # a = list(d)
    # with open("database/user.json", "w") as outfile:
    #     outfile.write(json.dumps(a))
    #     outfile.close()
    # return redirect('/menu')
    i = 0
    user = User(id=form['id'], first_name=form['fname'], last_name=form['lname'], email=form['email'])
    d = User.query.filter_by(id=form['id']).first()
    if User.query.filter_by(id=form['id']).first():
        i += 1
    if i > 0:
        d.id = form['id']
        d.first_name = form['fname']
        d.last_name = form['lname']
        d.email = form['email']
        db.session.commit()
        return redirect("/menu")
    elif i == 0:
        return "<h1>incorrect data</h1>"


@app.route('/add', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/choose', methods=['get'])
def choose():
    return render_template("delete.html")


@app.route('/delete', methods=['post'])
def delete():
    form = request.form
    # d = read()
    # f = d[0]
    # i = 0
    # for k in d:
    #     if str(k['id']) == form['id']:
    #         f = k
    # for k in range(0, len(d)):
    #     if d[k] == f:
    #         i = k
    # a = list(d)
    # a.pop(i)
    # with open("database/user.json", "w") as outfile:
    #     outfile.write(json.dumps(a))
    #     outfile.close()
    # return a
    d = User.query.filter_by(id=form['id']).first()
    if User.query.filter_by(id=form['id']).first():
        db.session.delete(d)
        db.session.commit()
        return redirect("/menu")
    else:
        return "<h1>incorrect data</h1>"


@app.route('/show', methods=['POST'])
def save():
    form = request.form
    # dictionary = {
    #     "first_name": form['fname'],
    #     "last_name": form['lname'],
    #     "Email": form['email'],
    #     "id": form['id']
    # }
    # d = read()
    # a = list(d)
    # a.append(dictionary)
    # with open("database/user.json", "w") as outfile:
    #     outfile.write(json.dumps(a))
    #     outfile.close()
    user = User(id=form['id'], first_name=form['fname'], last_name=form['lname'], email=form['email'])
    db.session.add(user)
    db.session.commit()
    return user.serialize


@app.route("/auhtorized", methods=["get"])
def auhtorized():
    return render_template('auhtorized.html')


@app.route('/auhtorized/successfully', methods=["post"])
def auhtorized_successfully():
    form = request.form
    # d = read()
    # t = form['passwords']
    # i = 0
    # f = 3
    # for k in d:
    #     if str(k['Email']) == str(form['email']) and k['password'] == form['passwords']:
    #         i = +1
    # if i > 0:
    #     return render_template('auhtorized_successfully.html')
    # elif i == 0:
    #     return "incorrect data"
    if User.query.filter_by(email=form['email']).first() and User.query.filter_by(password=form['passwords']).first():
        return render_template('auhtorized_successfully.html')
    else:
        return "<h1>incorrect data</h1>"


@app.route('/addcars', methods=['get'])
def add_car():
    return render_template("add-car.html")


@app.route('/add-car', methods=["post"])
def addcar_result():
    form = request.form
    # f = read_for_car()
    # dictionary = {
    #     'Brand': form['Brand'],
    #     'Type': form['Type'],
    #     'Number': form['Number'],
    #     'user_id': form['user_id']
    # }
    # a = list(f)
    # a.append(dictionary)
    # with open("database/cars.json", "w") as outfile:
    #     outfile.write(json.dumps(a))
    #     outfile.close()
    cars = Cars(Brand=form['Brand'], Type=form['Type'], Number=form['Number'], user_id=form['user_id'])
    db.session.add(cars)
    db.session.commit()
    return cars.serialize


@app.route("/change/car", methods=['get'])
def change_car():
    return render_template('change-car.html')


@app.route('/change-car', methods=['post'])
def after_change_car():
    form = request.form
    # # # dictionary = {
    # # #     'Brand': form['Brand'],
    # # #     'Type': form['Type'],
    # # #     'Number': form['Number'],
    # # #     'user_id': form['user_id']
    # # # }
    # # # d = read_for_car()
    # # # r = form['user_id']
    # # # h = d[0]
    # # # i = 0
    # # # z = 0
    # # # for k in d:
    # # #     if str(k['user_id']) == str(r):
    # # #         h = k
    # # #         z += 1
    # # # for k in range(0, len(d)):
    # # #     if h == d[k]:
    # # #         i = k
    # # # d[i] = dictionary
    # # # a = list(d)
    # # # if z > 0:
    # #     with open("database/cars.json", "w") as outfile:
    # #         outfile.write(json.dumps(a))
    # #         outfile.close()
    # #     return redirect('/showCars')
    # elif z == 0:
    i = 0

    d = Cars.query.filter_by(user_id=form['user_id']).first()
    if Cars.query.filter_by(user_id=form['user_id']).first():
        i += 1
    if i > 0:
        d.Brand = form['Brand']
        d.Type = form['Type']
        d.Number = form['Number']
        d.user_id = form['user_id']
        db.session.commit()
        return d.serialize
    elif i == 0:
        return "<h1>incorrect data</h1>"


@app.route('/delete-car', methods=["get"])
def delete_car():
    return render_template('delete-car.html')


@app.route('/delete/car', methods=["post"])
def after_delete_car():
    form = request.form
    # d = read_for_car()
    # f = d[0]
    # i = 0
    # l = 0
    # for k in d:
    #     if str(k['user_id']) == form['user_id']:
    #         f = k
    #         l += 1
    # for k in range(0, len(d)):
    #     if d[k] == f:
    #         i = k
    # a = list(d)
    # a.pop(i)
    # if l > 0:
    #     with open("database/cars.json", "w") as outfile:
    #         outfile.write(json.dumps(a))
    #         outfile.close()
    #     return a
    # elif l == 0:
    #     return "<h1>incorrect data</h1>"
    d = Cars.query.filter_by(user_id=form['user_id']).first()
    if User.query.filter_by(user_id=form['user_id']).first():
        db.session.delete(d)
        db.session.commit()
    else:
        return "<h1>incorrect data</h1>"


@app.route('/')
def da():
    return render_template('shapka.html')
