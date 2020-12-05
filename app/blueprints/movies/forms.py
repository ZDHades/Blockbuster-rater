from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

class Search_Movie(FlaskForm):
    name = StringField()
    submit = SubmitField('search')