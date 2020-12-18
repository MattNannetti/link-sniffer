from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    urlInput = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Get Started')