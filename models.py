from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text, select
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models go below
class Patient(db.Model):
    """Patients Model"""
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    disease = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    recipe = db.relationship('Recipe')


    
    def __repr__(self):
        return f"<Recipe {self.id} {self.first_name} {self.last_name} {self.age} >"

class Recipe(db.Model):
    """Healthy Recipe Model"""
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    recipe_name = db.Column(db.Text, nullable=False, unique=True)
    ingredients = db.Column(db.Text)

    patient = db.relationship('Patient')

    def __repr__(self):
        return f"<Recipe {self.recipe_name} {self.ingredients} >"
    





