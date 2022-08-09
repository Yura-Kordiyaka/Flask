import json
import request
from flask import Flask, render_template, request

app = Flask(__name__)


def read():
    with open('database/user.json', 'r') as f:
        g = f.read()
        data = json.loads(g)
        f.close()
    return data


@app.route('/')
def general():
    d = read()
    return d


@app.route('/add', methods=['GET'])
def index():
    return render_template("index.html")


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
