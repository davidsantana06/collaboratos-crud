from flask_wtf import FlaskForm
from wtforms import FloatField, StringField
from wtforms.validators import DataRequired, Length, NumberRange


class CreateForm(FlaskForm):
    first_name = StringField(validators=[DataRequired(), Length(1, 30)])
    last_name = StringField(validators=[DataRequired(), Length(1, 30)])
    participation = FloatField(validators=[DataRequired(), NumberRange(1, 100)])
