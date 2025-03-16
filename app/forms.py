from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired  

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class UploadForm(FlaskForm):
    file = FileField('Upload Image', validators=[
        FileRequired(message='Please select a file'),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Only images allowed! (jpg, png)')
    ])
    submit = SubmitField('Upload')