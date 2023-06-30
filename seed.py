from models import Recipe, Patient, db
from app import app

#create tables
db.drop_all()
db.create_all()

r1 = Recipe(recipe_name='Greek Shrimp & Orzo', 
            ingredients='2lb shrimp, 1/2 cup lemon juice, 3/4lb orzo pasta uncooked, 1/2 cup scallions sliced, 3/4 cup parsley, 3/4 cup fresh dill, 1 cup feta cheese')

p1 = Patient(first_name='Michael', last_name='Aylmer')

db.session.add(r1)

db.session.add(p1)

db.session.commit()