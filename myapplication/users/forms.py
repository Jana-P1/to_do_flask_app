from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SubmitField, PasswordField


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email')
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', [validators.DataRequired()])
    submit = SubmitField('Register')