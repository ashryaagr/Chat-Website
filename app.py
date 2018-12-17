import os
from flask import Flask, render_template, request, flash
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
    
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

socketio = SocketIO(app)

db = SQLAlchemy(app)
""" class user(db.Model) :
    __table__="user"
    display_name = db.column(db.String)
    password = db.column(db.String)
    email = db.column(db.String) """

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/login")
def login() :
    return login.html

@app.route("/account_creation", methods=["POST"])
def account_creation():
    name = request.form.get("InputDisplayName")
    email = request.form.get("InputEmail1")
    password = request.form.get("InputPassword1")
    if email in :
        messsage = "Sorry the Email already exists in our DATABASE. Please try with some other Email"
        return render_template("account_creation.html", message=message)
    else :
        flash('account sucessfully created')
        return login()

if __name__=="__main__" :
    app.run()