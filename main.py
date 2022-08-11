import json
import request
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def read():
    with open('database/user.json', 'r') as f:
        g = f.read()
        data = json.loads(g)
        f.close()
    return data


@app.route('/', methods=['Get'])
def general():
    d = read()
    return d


@app.route('/search', methods=['Get'])
def search_email():
    return render_template("search.html")


@app.route('/result/search', methods=['post'])
def result_search():
    form = request.form
    d = read()
    i = 0
    h = d[0]
    for k in d:
        if str(k['Email']) == form['email']:
            h = k
            i = i + 1
    if i > 0:
        return h
    elif i == 0:
        return "incorrect data"


@app.route('/change', methods=['GET'])
def change():
    return render_template('change.html')


@app.route('/after_change', methods=['post'])
def after_change():
    form = request.form
    dictionary = {
        "first_name": form['fname'],
        "last_name": form['lname'],
        "Email": form['email'],
        "id": form['id'],
    }
    d = read()
    h = d[0]
    i = 0
    for k in d:
        if str(k['id']) == form['id']:
            h = k
    for k in range(0, len(d)):
        if h == d[k]:
            i = k
    d[i] = dictionary
    a = list(d)
    with open("database/user.json", "w") as outfile:
        outfile.write(json.dumps(a))
        outfile.close()
    return redirect('/')


@app.route('/add', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/choose', methods=['get'])
def choose():
    return render_template("delete.html")


@app.route('/delete', methods=['post'])
def delete():
    form = request.form
    d = read()
    f = d[0]
    i = 0
    for k in d:
        if str(k['id']) == form['id']:
            f = k
    for k in range(0, len(d)):
        if d[k] == f:
            i = k
    a = list(d)
    a.pop(i)
    with open("database/user.json", "w") as outfile:
        outfile.write(json.dumps(a))
        outfile.close()
    return a


@app.route('/show', methods=['POST'])
def save():
    form = request.form
    dictionary = {
        "first_name": form['fname'],
        "last_name": form['lname'],
        "Email": form['email'],
        "id": form['id']
    }
    d = read()
    a = list(d)
    a.append(dictionary)
    with open("database/user.json", "w") as outfile:
        outfile.write(json.dumps(a))
        outfile.close()
    return "Your last add \n" + str(a[-1])


@app.route("/auhtorized", methods=["get"])
def auhtorized():
    return render_template('auhtorized.html')


@app.route('/auhtorized/successfully', methods=["post"])
def auhtorized_successfully():
    form = request.form
    d = read()
    t = form['passwords']
    i = 0
    f = 3
    for k in d:
        if str(k['Email']) == str(form['email']) and k['password'] == form['passwords']:
            i = +1
    if i > 0:
        return render_template('auhtorized_successfully.html')
    elif i == 0:
        return "incorrect data"


if __name__ == "__main__":
    app.run(debug=True)
