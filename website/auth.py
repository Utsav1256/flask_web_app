from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(name) < 2:
            flash("Name must be greater than 1 character.", category="error")

        elif password != confirm_password:
            flash("Passwords dont't match.", category="error")

        elif len(password) < 7:
            flash("Password must be greater than 7 characters.", category="error")

        else:
            # add user to database
            new_user = User(
                email=email,
                name=name,
                password=generate_password_hash(password, method="sha256"),
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!", category="success")

            # redirecting to homepage
            return redirect(url_for("views.home"))
    return render_template("sign_up.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"
