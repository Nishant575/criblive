from random import choices
from flask_wtf import FlaskForm  
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from hp import util

class InfoForm(FlaskForm):
    area = IntegerField('Area (in Sqft.)',
                        validators=[DataRequired()])
    bhk = SelectField('BHK', choices=[1,2,3,4,5], coerce=int)
    bath = SelectField('Bath', choices=[1,2,3,4,5], coerce=int)
    location = SelectField('Location', choices=util.get_location_names())
    submit = SubmitField('Predict')

class buyform(FlaskForm):
    loc = SelectField('Location', choices=util.get_location_names())
    submit = SubmitField('Price Trend')