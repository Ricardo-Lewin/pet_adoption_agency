from typing import Optional
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import Optional, InputRequired, URL, NumberRange, Length


class PetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species")
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age (optional)", validators=[
                       Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes (optional)", validators=[
                        Optional(), Length(min=10)])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = StringField(
        "Notes",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")
