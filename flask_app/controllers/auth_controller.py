from flask import session, request, render_template, redirect, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


# @app.route('/login', methods=['GET'])
# def login_form():
#     return render_template("auth/login.html")


# @app.route('/login', methods=['POST'])
# def login_authenticate():
#     data = { "email" : request.form["email"] }
#     user_in_db = User.get_by_email(data)
#     if not user_in_db:
#         flash("Invalid Email/Password")
#         return redirect("/login")
#     if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
#         flash("Invalid Email/Password")
#         return redirect('/login')
    
#     session['user_id'] = user_in_db.id
#     return redirect("/users")


# @app.route("/register", methods=["GET"])
# def register_form():
#     return render_template("auth/create_user.html")


# @app.route("/register", methods=["POST"])
# def create_user():
#     pw_hash = bcrypt.generate_password_hash(request.form['password'])
#     print(pw_hash)
#     data = {
#         "email": request.form["email"],
#         "user_name": request.form['user_name'],
#         "password" : pw_hash
#     }
#     user_id = User.save(data)
#     session['user_id'] = user_id
#     return redirect("/my-gallery")


# @app.route("/logout1")
# def logout1():
#     session.clear()
#     return redirect('/login')