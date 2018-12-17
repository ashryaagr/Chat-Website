import os
from flask import Flask, render_template, request, flash, session, abort, redirect, jsonify
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from models import *

app = Flask(__name__)
#app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/account_creation", methods=["POST"])
def account_creation():
    name = request.form.get("InputDisplayName")
    email = request.form.get("InputEmail1")
    password = request.form.get("InputPassword1")
    """ if email in db.email:
        message = "Sorry the Email already exists in our DATABASE. Please try with some other Email"
        return render_template("account_creation.html", message=message)
    else :
        flash('account sucessfully created') """
    return login()

if __name__=="__main__" :
    app.run()
