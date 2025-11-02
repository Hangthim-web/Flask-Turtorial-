from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,length

0
class RegistrationForm(FlaskForm):
    name = StringField("Full Name",validators = [DataRequired()])
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired(),length(min=6)])
    submit = SubmitField("Register")