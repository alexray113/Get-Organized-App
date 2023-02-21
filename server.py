"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)

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
    return render_template('starting-page.html')

#app route to create user page
@app.route("/create-account")
def display_create_account():
    """Loads account creation page"""

    return render_template("create-account.html")

# app route to errands page
@app.route("/maps")
def view_map():
    """Load the homepage."""
# renders maps.html template
    return render_template('maps.html')

# app route to login page
@app.route('/user_login')
def display_login():
    """Display Login Page."""
# renders user_login.html template
    return render_template('user_login.html')

# app route to braindumps page
@app.route('/braindump')
def display_braindump():
    """Displays braindump page"""
# renders braindump.html template
    return render_template('braindump.html')

# app route to reminders page
@app.route('/reminders')
def display_reminders():
    """Displays reminders page"""
# renders reminders.html template
    return render_template('reminders.html')

# app route to to-dos page
@app.route('/to-dos')
def display_to_dos():
    """Displays reminders page"""
# renders to-do-items.html template
    return render_template('to-do-items.html')

# app route to return to user dashboard from maps, braindumps, and reminders page
@app.route('/dashboard')
def display_user_profile():
    """Returns to dashboard of user in session"""
# retrieves user info from session to stay logged in

    if 'user_id' not in session:
        return redirect("/user_login")

    user_id = session['user_id']
    return redirect(f'/users/{user_id}') 
        
    
    # app route to display user dashboard page
@app.route('/users/<user_id>')
def show_user(user_id):
    """Display user profile page"""
    # saves user object to get_user_by_id by using crud.py function to query
    # user database
    user_object = crud.get_user_by_id(user_id)
    # pulls user email, id, and first name from user object
    user_email = user_object.email
    user_id = user_object.user_id
    user_fname = user_object.fname

# make a list of all user reminders and add to list
    # user_reminders = crud.get_reminder_by_id(user_id)
    user_to_dos = crud.get_to_do_by_id(user_id)
            

# make a list of all user braindumps and add to list
    user_bds = crud.get_bd_by_id(user_id)

    
    # renders user_profile.html template and passes user object info, reminder list,
    # and bd list to jinja template variables
    return render_template('user_profile.html', user_id=user_id, user_email=user_email, user_fname=user_fname, user_to_dos=user_to_dos, user_bds=user_bds)
   

@app.route("/login", methods=['POST'])
def login_user():
    """Logs user in"""
    # pulls email input from form on homepage.html and saves to user_email variable
    user_email= request.form.get('email')
    # pulls password input from form on homepage.html and saves to password varialbe
    password = request.form.get('password')
    # uses post request variable as argument for get_user_by email crud.py function
    # to query user database and save user_object to variable user object
    user_object = crud.get_user_by_email(user_email)
    if user_object:
    # saves user_object password, user id, email, and first name to variables
        db_password = user_object.password
        user_id = user_object.user_id
        user_fname = user_object.fname

        if password == db_password:
            # stores id in session and logs user in if input password matches
            # database password
            session['user_id'] = user_id
            session['email'] = user_email
            session['fname'] = user_fname
            
            # flashes statement indicating login successful
            flash("You have logged in successfully!")
            # redirects to user profile page
            return redirect(f'/users/{user_id}')
        else:
            # flashes statement indicating password is incorrect
            flash("Login password incorrect.")
    else:
        flash("No user found. Please create an account.")
 
    
    return render_template("user_login.html")

# app route to log user out
@app.route("/logout")
def logout():
    """ Log out """
    # clears session is user is logged in and flashes success message
    if "user_id" in session:
        session.clear()
        flash("You have been logged out successfully. Please come back soon!")
    
    return redirect("/")

# app route to create account page
@app.route('/create-account', methods=['POST'])
def user_sign_up():
    """Check if user email already in database, if not, create a new user profile."""
    # pulls fname input from login form on homepage.html and saves to user_fname
    # variable
    user_fname = request.form.get('fname')
    # pulls fname input from login form on homepage.html and saves to user_fname
    # variable
    user_lname = request.form.get('lname')
    # pulls lname input from login form on homepage.html and saves to user_lname
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
        new_user = crud.create_user(user_fname, user_lname, user_email, password)
        # adds new user to db
        db.session.add(new_user)
        # commits new user to db and then flashes success message
        db.session.commit()
        flash('Your account was created successfully! You are now logged in.')
    
    # pulls user id from user object and saves in session
    user_id = new_user.user_id
    session['user_id'] = user_id
    user_email = new_user.email
    session['user_email'] = user_email


    # redirects to user profile when sign up is successful and flashes appropriate message
    return redirect(f'/users/{user_id}') 

@app.route('/create-to-do', methods=["POST"])
def create_to_do():
    # gets user id from session and pulls text from bd input form
    user_id = session['user_id']
    to_do = request.form.get("to-do")
    # calls crud function to store new braindump in database and saves to varialbe
    to_do = crud.create_user_to_do(user_id, to_do)
                                        
    # adds braindump to database
    db.session.add(to_do)
    db.session.commit()


    return redirect('/to-dos')

# allows user to delete reminders
@app.route("/delete-to-do", methods=['POST']) 
def delete_to_do():
    
    to_do_id = int(request.json.get("btn_id"))
    print(to_do_id)
    print("************")
    delete_to_do = crud.delete_to_do(to_do_id)
    
    return delete_to_do

@app.route('/submit_bd', methods=["POST"])
def create_bd():
    # gets user id from session and pulls text from bd input form
    user_id = session['user_id']
    text_body = request.form.get("bd_content")
    # calls crud function to store new braindump in database and saves to varialbe
    braindump = crud.create_braindump(user_id, text_body)
                                        
    # adds braindump to database
    db.session.add(braindump)
    db.session.commit()


    return redirect('/braindump')


#allows user to edit braindump
@app.route("/edit-braindump", methods=['POST'])
def edit_bds():

    bd_id = request.form.get("bd_id")
    bd_object = crud.return_bd_by_id(bd_id)
    bd_text = bd_object.text_body

    return render_template("saved_braindumps.html", bd_text=bd_text, bd_id=bd_id)

@app.route("/update-bd", methods=['POST'])
def update_bds():
    user_id = session['user_id']
    text_body = request.form.get("edit-bd-text")
    bd_id = int(request.form.get("bd_id"))
    
    updated_bd = crud.update_bd_by_id(bd_id, text_body)

    return redirect(f'/users/{user_id}') 

        

@app.route("/delete-braindumps", methods=['POST'])
def delete_bds():

    bd_id = int(request.json.get("bd_btn_id"))
    print(type(bd_id))
    delete_braindump = crud.delete_bd(bd_id)

    return delete_braindump







if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)