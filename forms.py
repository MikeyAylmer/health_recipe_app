from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import InputRequired, Email, email_validator, Optional



class AddRecipeForm(FlaskForm):
    """Form for adding snack"""
    name = StringField('Recipe Name')
    ingredients = StringField('Ingredients list')
    recipe_diff = FloatField('1-10 Diff of recipe')

class PatientForm(FlaskForm):
    """Form for adding patient"""
    Email = StringField("Email", validators=[Optional(), Email()])
    first_name = StringField("Patient First Name", validators=[InputRequired(message="Patient Name Can't Be Empty")])
    last_name = StringField("Patient Last Name")
    disease = StringField('Disease Name')
    age = IntegerField("Patient Age", validators=[InputRequired(message="Please Enter Valid Age")])