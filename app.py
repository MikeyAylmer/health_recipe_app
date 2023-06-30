from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Recipe, Patient
from sqlalchemy.sql import text
from forms import AddRecipeForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///healthcare_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Sunniva2023'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/', methods=["GET", "POST"])
def add_recipe():
    form = AddRecipeForm()
    return render_template('add_recipe_form.html', form=form)