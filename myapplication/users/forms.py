from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SubmitField, PasswordField, ValidationError
from myapplication.models.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', [validators.DataRequired()])
    submit = SubmitField('Register')

# checks if the email has already been registered to another user
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("That email has already been registered to another user. Please use a different email!")
        

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Log In')