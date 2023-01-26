"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# app route to homepage
@app.route("/")
def view_homepage():
    """Load the homepage."""
# renders homepage.html template
    return render_template('homepage.html')

@app.route('/user_login')
def display_login():
    """Display Login Page."""

    return render_template('user_login.html')

@app.route('/braindump')
def display_braindump():
    """Displays braindump page"""

    return render_template('braindump.html')

@app.route('/reminders')
def display_reminders():

    return render_template('reminders.html')

@app.route('/user_profile')
def display_user_profile():

    return render_template('user_profile.html')

@app.route('/users/<user_id>')
def show_user(user_id):
    """Display user profile page"""
    # saves user object to get_user_by_id by using crud.py function to query
    # user database
    get_user_by_id = crud.get_user_by_id(user_id)
    # renders user_profile.html template and passes user object (get_user_by_id) to
    # html jinja template variable user
    return render_template('user_profile.html', user=get_user_by_id)

@app.route("/login", methods=['POST'])
def login_user():
    # pulls email input from form on homepage.html and saves to user_email variable
    user_email= request.form.get('email')
    # pulls password input from form on homepage.html and saves to password varialbe
    password = request.form.get('password')
    # uses post request variable as argument for get_user_by email crud.py function
    # to query user database and save user_object to variable user object
    user_object = crud.get_user_by_email(user_email)
    # saves user_object password to variable db_password
    db_password = user_object.password
    # saves user_id from user_object to variable user_id
    user_id = user_object.user_id
    print(password)
    print(db_password)
    if password == db_password:
        # stores id in session and logs user in
        session['user_id'] = user_id
        # flashes statement indicating login successful
        flash("You have logged in successfully!")
         # redirects to user profile page and flashes appropriate message
        return redirect(f'/users/{user_id}')
    else:
        # flashes statement indicating login successful
        flash("Login password incorrect.")
    
    return render_template("user_login.html")

# app route to / using POST method
@app.route('/users', methods=['POST'])
def user_sign_up():
    """Check if user email already in database, if not, create a new user profile."""
    # pulls email input from login form on homepage.html and saves to user_email
    # variable
    user_email= request.form.get('email')
    # pulls password input from login form on homepage.html and saves to password
    # variable
    password = request.form.get('password')
    # passes user_email variable to get_user_by_email crud.py function to query
    # database and check for existence of user
    if crud.get_user_by_email(user_email):
        # if user exists flashes message
        flash('This user already exists. Please enter a new email.')
        return redirect('/')
    else:
        # if user doesn't exist, calls create_user crud.py function and passes
        # POST request variables as arguments to create new user. Saves to new_user
        # variable
        new_user = crud.create_user(user_email, password)
        # adds new user to db
        db.session.add(new_user)
        # commits new user to db and then flashes success message
        db.session.commit()
        flash('Your account was created successfully! You may now login.')
    
    user_id = new_user.user_id
    session['user_id'] = user_id


    # redirects to user profile upon completion and flashes appropriate message
    return redirect(f'/users/{user_id}') 

#app route to /users 
@app.route('/users')
def show_all_users():
    """Display email address of each user with link to user profile"""
    # returns list of all users and saves to all_users variable by calling
    # return_all_users function in crud.py file
    all_users = crud.return_all_users()
    # renders users.html template and sends user list to all_users variable in users.html
    # jinja template
    return render_template('users.html', all_users=all_users)




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)