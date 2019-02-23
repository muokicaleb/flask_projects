from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired


class inputForm(FlaskForm):
    kg = IntegerField('Kg', validators=[DataRequired()])
    cm = IntegerField('Cm', validators=[DataRequired()])
    submit = SubmitField('Calculate')
