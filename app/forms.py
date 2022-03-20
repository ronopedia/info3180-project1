from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    bedroom = StringField('No. of Rooms', validators=[DataRequired()])
    bathroom = StringField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'],'Images Only!')])
    description = TextAreaField('Description', validators=[DataRequired()])
    proptype= SelectField('Property Type', choices=[(1,'House'), (2,'Apartment')], validators=[DataRequired()])