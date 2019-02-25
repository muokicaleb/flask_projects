from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import IntegerField, SubmitField


class input(FlaskForm):
    weight = IntegerField('Weight in kg', validators=[DataRequired()])
    height = IntegerField('Height in cm', validators=[DataRequired()])
    submit = SubmitField('Calculate')
