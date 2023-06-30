from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class AddRecipeForm(FlaskForm):
    """Form for adding snack"""
    name = StringField('Recipe Name')
    ingredients = StringField('Ingredients list')
    recipe_diff = FloatField('1-10 Diff of recipe')