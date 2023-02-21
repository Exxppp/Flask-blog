from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Regexp, EqualTo, Length

from utils.regex import EMAIL, USERNAME


class UserRegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(4, 32)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(4, 32)])
    username = StringField('Username', validators=[DataRequired(), Regexp(USERNAME)])
    email = EmailField('Email', validators=[DataRequired(), Regexp(EMAIL)])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match'), Length(6, 128)])
    password2 = PasswordField('Repeat password', validators=[DataRequired()])


class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Regexp(USERNAME)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 128)])


class WriteBlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
