"""CRUD operations."""

from model import db, User, User_to_dos, User_reminder, Brain_dump, connect_to_db

# user functions
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

# brain dump functions

def create_braindump(user_id, bd_title, text_body):

    braindump = Brain_dump(user_id=user_id, bd_title=bd_title, text_body=text_body)

    return braindump

def delete_bd(bd_id):

    bd = Brain_dump.query.get(bd_id)
    db.session.delete(bd)
    db.session.commit()

    return print("**********Deleted Successfully!********")

def get_bd_by_id(user_id):
    """Get and return braindumps by ID"""

    return Brain_dump.query.filter_by(user_id=user_id).all()

def return_bd_by_id(bd_id):
    """Get and return braindump by ID"""

    return Brain_dump.query.get(bd_id)

def update_bd_by_id(bd_id, text_body):

    bd = Brain_dump.query.get(bd_id)
    bd.text_body = text_body
    db.session.commit()

    return "Updated Successfully!"

# to do functions
def create_user_to_do(user_id, to_do_item):

    to_do = User_to_dos(user_id=user_id, 
            to_do_item=to_do_item)

    return to_do

def delete_to_do(to_do_id):

    to_do = User_to_dos.query.get(to_do_id)
    db.session.delete(to_do)
    db.session.commit()

    return print("Deleted Successfully!")

def get_to_do_by_id(user_id):
    """Get and return to dos by ID"""

    return User_to_dos.query.filter_by(user_id=user_id).all()
    
if __name__ == '__main__':
    from server import app
        
    connect_to_db(app)