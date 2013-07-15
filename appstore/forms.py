from wtforms import Form, BooleanField, TextField, validators, TextAreaField, PasswordField
from flask.ext.wtf import Required

class AddAppForm(Form):
    name     = TextField('Name', [validators.Length(min=4, max=25)])
    category  = TextField('Category', [validators.Length(min=4, max=35)])
    description = TextAreaField('Desciption', [validators.Length(min=0, max=400)])

class OpenIDLoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class LoginForm(Form):
	name = TextField('name', [validators.Length(min=4, max=25)])
	password = PasswordField('password', [validators.Length(min=4, max=30)])

class RegisterForm(Form):
	name = TextField('name', [validators.Length(min=4, max=25)])
	email = TextField('email', [validators.Length(min=4, max=25)])
	password = PasswordField('password', [validators.Length(min=4, max=30)])
	remember_me = BooleanField('remember_me', default = False)
    