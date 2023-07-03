from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Recipe, Patient
from sqlalchemy.sql import text
from forms import AddRecipeForm, PatientForm

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
    # for CSRF token validation
    if form.validate_on_submit():
        name = form.name.data
        ingredients = form.ingredients.data
        difficulty = form.recipe_diff.data
        flash(f"Created new recipe: {name} {ingredients} Difficulty rating is {difficulty} ")
        return redirect('/details')
    else:
        return render_template('add_recipe_form.html', form=form)
    
@app.route('/details')
def details_page():
    """details for recipe"""
    return render_template('details.html')

@app.route('/patients', methods=['GET', "POST"])
def show_list_of_patients():
    """Renders patient list"""
    pats = Patient.query.all()
    return render_template('patients.html', pats=pats)

@app.route('/patients/new', methods=["GET", "POST"])
def add_new_patients():
    """page to add patients"""
    form = PatientForm()
    if form.validate_on_submit():

        first_name = form.first_name.data
        last_name = form.last_name.data
        disease = form.disease.data
        age = form.age.data

        patient = Patient(first_name=first_name, last_name=last_name, disease=disease, age=age)

        db.session.add(patient)
        db.session.commit()

        return redirect('/patients')
    else:
        return render_template('add_patient_form.html', form=form)
    
@app.route('/patients/<int:id>/edit', methods=['GET', 'POST'])
def edit_patient(id):
    """Form to edit patient"""
    user = Patient.query.get_or_404(id)
    form = PatientForm(obj=user)
    pats = db.session.query(Patient.first_name, Patient.disease, Patient.age)
    form.first_name.choices = pats

    if form.validate_on_submit():
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.age = form.age.data

        db.session.commit()
        return redirect('/patients')
    else:
        return render_template('edit_patient_form.html', form=form)