import os
from flask import Flask, render_template, request, flash, session, abort, redirect, jsonify, session, url_for
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import flask_login
from models import *
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("ashryaagrdeveloper@gmail.com", "#####")

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

socketio = SocketIO(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

def main():
    db.create_all()

@app.route("/")
def index():
    if 'username' in session:
        pass
    else :
        return render_template("index.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/account_creation")
def account_creation():
    name = request.form.get("InputDisplayName")
    email = request.form.get("InputEmail1")
    password = request.form.get("InputPassword1")
    user = User(display_name=name, email=email, password=password)
    if User.query.filter_by(email=email) :
        message = "Sorry the Email already exists in our DATABASE. Please try with some other Email"
        return render_template("account_creation.html", message=message)
    message = "You have tried to register for the online messaging service : FLACK . I assure you that best possible services shall be provided to you ."
    server.send_message("ashryaagrdeveloper@gmail.com", email, message)
    flash('account sucessfully created')
    return render_template("login.html")

if __name__== "__main__" :
    app.run(debug=True)
