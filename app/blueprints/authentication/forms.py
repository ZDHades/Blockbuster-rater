from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, EqualTo, email_validator
from flask_wtf import FlaskForm

class Register(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    email = StringField(validators=[Email(message='Not a valid email address')])
    password = PasswordField()
    confirm_password = PasswordField(EqualTo('password'))
    submit = SubmitField('Register')

class Login(FlaskForm):
    email = StringField(validators=[Email(message='Not a valid email address')])
    password = PasswordField()
    submit = SubmitField('Login')

