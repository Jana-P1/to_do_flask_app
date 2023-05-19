import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash,generate_password_hash
from myapplication import db

from myapplication.models.models import User, ToDo

users = Blueprint('users', __name__)

@users.route('/signup', methods=["GET", "POST"])
def signup():
    print("sign Up")