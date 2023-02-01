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

# reminder types
reminder_text = crud.create_reminder_type('text')
model.db.session.add(reminder_text)
reminder_email = crud.create_reminder_type('email')
model.db.session.add(reminder_email)
reminder_push = crud.create_reminder_type('push')
model.db.session.add(reminder_push)
reminder_contact = crud.create_reminder_type('contact')
model.db.session.add(reminder_contact)
model.db.session.commit() 


# loop that generates ten user objects

fnames = ['Joe', 'Sally', 'Alex', 'Roger', 'Bob', 'Jerry', 'Jenna', 'Susie', 'Cindy', 'Mike']
lnames = ['Smith', 'Rogers', 'Davids', 'Martinez', 'Jacobson', 'Jeffries', 'Lopez', 'Rodriguez', 'Simon', 'Phillips']
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'
    fname = fnames[n]
    lname = lnames[n]


    # create a User object with above data
    new_user = crud.create_user(fname, lname, email, password)

    model.db.session.add(new_user)




    model.db.session.commit()  