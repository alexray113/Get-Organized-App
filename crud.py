"""CRUD operations."""

from model import db, User, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

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

    if __name__ == '__main__':
        from server import app
        connect_to_db(app)