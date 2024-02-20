from flask_wtf import FlaskForm
from wtforms import FloatField, StringField
from wtforms.validators import DataRequired, Length, NumberRange


class CreateForm(FlaskForm):
    first_name = StringField(name="first-name", validators=[DataRequired(), Length(1, 30)])
    last_name = StringField(name="last-name", validators=[DataRequired(), Length(1, 30)])
    participation = FloatField(name="participation", validators=[DataRequired(), NumberRange(1, 100)])
