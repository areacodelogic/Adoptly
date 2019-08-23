from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):

    name = StringField("Pet Name",
                       validators=[InputRequired()])

    species = StringField("Species",
                          validators=[InputRequired()])

    photo_url = StringField("Photo URL",
                            validators=[Optional()])

    age = IntegerField("Age",
                       validators=[InputRequired()])

    notes = StringField("Notes",
                        validators=[Optional()])

    # available = BooleanField('Available',
    #                          validators=[Optional()])
