from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, IntegerField, BooleanField, SubmitField


class input(FlaskForm):
    Weight = IntegerField('Weight in kg', validators=[DataRequired()])
    height = IntegerField('Height in cm', validators=[DataRequired()])
    submit = SubmitField('Calculate')
