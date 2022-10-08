from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Your email', validators=[DataRequired()])
    password = PasswordField('Your password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class TaskForm(FlaskForm):
    task = StringField('Add a task', validators=[DataRequired()])
    submit = SubmitField('Submit')