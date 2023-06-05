import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werkzeug.security import check_password_hash,generate_password_hash
from myapplication.db import db_session  


# myapplication related imports
from myapplication.models.models import User, ToDo
from myapplication.users.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)

# Allows users to signup
@users.route('/signup', methods=["GET", "POST"])
def signup():
    form = RegistrationForm()
    if form.validate() and request.method == "POST":
        user = User(username=form.username.data, 
                    email=form.email.data, 
                    password=form.password.data
                    )
        db_session.add(user)
        db_session.commit()
        print("Thanks for signing up!")
        return redirect(url_for('users.login'))
    
    return render_template("signup.html", form=form)



# Logs in registered users
@users.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    # print("login: Sanity Check")
    if request.method == "POST" and form.validate_on_submit():
        user = db_session.query(User).filter_by(username=form.username.data).first()
        print(user)
        error = None
        if user is None:
            error = "Username is incorrect. Please re-type your username."
            print(error)
        elif not check_password_hash(user['password'], user.password):
            error = "Password is incorrect. Please re-type your password."
            print(error)
        
        if error is None:
            print("You're logged in!")
            return redirect(url_for('landing.index'))
           
    return render_template('login.html', form=form)


