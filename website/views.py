from flask import Blueprint, render_template, current_user
from flask_login import login_required

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/pofile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)
