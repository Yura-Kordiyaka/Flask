from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://yura:parol@localhost:3306/flask'
db = SQLAlchemy(app)
db.init_app(app)





with app.app_context():
    from rootes.roots import *
    from models import Cars, User
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
