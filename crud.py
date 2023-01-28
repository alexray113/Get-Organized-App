"""CRUD operations."""

from model import db, User, Reminder, User_reminder, User_contact, Brain_dump, User_news, Positive_news, connect_to_db


def create_user(fname, lname, email, password):
    """Create and return a new user."""

    user = User(fname=fname, lname=lname, email=email, password=password)

    return user

def return_all_users():
    """Return list of all users"""

    return User.query.all()

def get_user_by_id(user_id):
    """Get and return user by ID"""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Get and return user by ID"""

    return User.query.filter(User.email == email).first()

def create_reminder_type(type):

    reminder_type = Reminder(type=type)

    return reminder_type

def create_user_reminder(reminder_id, user_id, creation_date, reminder_date, reminder_frequency, reminder_measure):

    reminder = User_reminder(reminder_id=reminder_id, user_id=user_id, creation_date=creation_date, reminder_date=reminder_date, reminder_frequency=reminder_frequency, reminder_measure=reminder_measure)

    return reminder

    if __name__ == '__main__':
        from server import app
        connect_to_db(app)