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


@app.route('/change', methods=['GET'])
def change():
    return render_template('change.html')


@app.route('/after_change', methods=['post'])
def after_change():
    form = request.form
    dictionary = {
        "Email": form['email'],
        "first_name": form['fname'],
        "id": form['id'],
        "last_name": form['lname']
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


if __name__ == "__main__":
    app.run(debug=True)
