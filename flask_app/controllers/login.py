from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models import login
from flask_bcrypt import Bcrypt
import random
from flask import flash
bcrypt = Bcrypt(app)

from datetime import datetime





@app.route("/user/create")
def CreateUser():
    

    return render_template("/pages/login.html")

@app.route("/register/create", methods=["POST"])
def MakeUser():
    if not login.Login.validate_order(request.form):
        return redirect("/user/create")
    print(request.form["Password"])
    data = {
        "first_name": request.form["Fname"],
        "last_name": request.form["Lname"],
        "email" : request.form["Email"],
        "password" :bcrypt.generate_password_hash(request.form["Password"])
    }
    result = login.Login.register(data)
    print(result)
    return redirect("/user/create")

@app.route("/login", methods= ['POST'])
def display_users():
    user = login.Login.get_by_email(request.form)
    if not user:
        flash("incorrect Email", "login")
        return redirect("/user/create")
    if not bcrypt.check_password_hash(user.password, request.form["Password"]):
        flash("incorrect password", "login")
        return redirect("/user/create")
    session["user_id"] = user.id
    return redirect("/browse/0")

# @app.route("/user_page")
# def edit_user():
#     if "user_id" not in session:
#         return redirect("/user/create")
#     data ={
#         "id" : session["user_id"]
#     }
#     user = login.Login.acquire_user(data)
#     return render_template("show_user.html", user= user)

# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect("/user/create")


