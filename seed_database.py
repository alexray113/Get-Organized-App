"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

# run these commands in the terminal
os.system('dropdb reminders')
os.system('createdb reminders')

# run these functions from model.py
model.connect_to_db(server.app)
model.db.create_all()

# loop that generates ten user objects
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # create a User object with above data
    new_user = crud.create_user(email, password)

    model.db.session.add(new_user)


model.db.session.commit()  