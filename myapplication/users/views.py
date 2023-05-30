import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werkzeug.security import check_password_hash,generate_password_hash
from myapplication import db  


# myapplication related imports
from myapplication.models.models import User, ToDo
from myapplication.users.forms import RegistrationForm, LoginForm

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
    form = LoginForm()
    print("login: Sanity Check")
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        pwhash = getattr(user, 'password_hash')
        check_password = check_password_hash(pwhash, form.password.data)

        if check_password and user is not None:
            session.clear()
            session['user_id'] = user['id']
            flash('Successfully logged in!')
            return redirect(url_for('landing.index'))
    return render_template('login.html', form=form)


        
       
            

    