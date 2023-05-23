import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash,generate_password_hash
from myapplication import db

from myapplication.models.models import User, ToDo
from myapplication.users.forms import RegistrationForm

users = Blueprint('users', __name__)

@users.route('/signup', methods=["GET", "POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, 
                    email=form.email.data, 
                    password=form.password.data
                    )
        db.db_session.add(user)
        db.db_session.commit()
        print("Thanks for signing up!")
        return redirect(url_for('users.login'))
    
    return render_template("signup.html", form=form)

@users.route('/login', methods=["GET", "POST"])
def login():
    print("login: Sanity Check")
    return render_template("login.html")