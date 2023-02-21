from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True, nullable=False)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50),nullable=False)

    user_reminder = db.relationship("User_reminder", back_populates="user")
    user_r = db.relationship("Brain_dump", back_populates="user")
    user_to_do = db.relationship("User_to_dos", back_populates="user")
    

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Reminder(db.Model):
    """A type of reminder"""

    __tablename__ = "reminder"

    reminder_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type = db.Column(db.String(50))

    reminder_rel = db.relationship("User_reminder", back_populates="reminder")

    def __repr__(self):
        return f'<Reminders reminder_id{self.reminder_id} type={self.type}>'

class User_to_dos(db.Model):
    """User's stored to do list items"""

    __tablename__ = "user_to_dos"

    to_do_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    to_do_item = db.Column(db.String(100))

    user = db.relationship("User", back_populates="user_to_do")

    def __repr__(self):
        return f'<User_To_Do to_do_id={self.to_do_id} user_id={self.user_id}>'



class User_reminder(db.Model):
    """User's stored reminders"""

    __tablename__ = "user_reminder"

    ur_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    reminder_id = db.Column(db.Integer, db.ForeignKey('reminder.reminder_id'))
    reminder_name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))      
    reminder_date = db.Column(db.DateTime)
    reminder_frequency = db.Column(db.Integer)
    reminder_measure = db.Column(db.String(30))

    user = db.relationship("User", back_populates="user_reminder")
    reminder = db.relationship("Reminder", back_populates='reminder_rel')

    def __repr__(self):
        return f'<User_Reminder ur_id={self.ur_id} user_id={self.user_id}>'

class Brain_dump(db.Model):
    """Stores user's brain dumps"""

    __tablename__ = "brain_dump"

    bd_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    text_body = db.Column(db.Text)

    user = db.relationship("User", back_populates="user_r")
    
    def __repr__(self):
        return f'<Brain_Dump bd_id={self.bd_id} user_id={self.user_id}>'

class User_news(db.Model):
    """Stores user's saved news articles"""

    __tablename__ = "user_news"

    saved_article_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('positive_news.article_id'), nullable=False)
    comment_id = db.Column(db.Text)

    art_id = db.relationship('Positive_news', back_populates="art_id")

    def __repr__(self):
        return f'<User_news saved_article_id={self.saved_article_id} user_id={self.user_id}>'

class Positive_news(db.Model):
    """Stores positive news articles"""

    __tablename__ = "positive_news"

    article_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    text_body = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(50), nullable=False)

    art_id = db.relationship('User_news', back_populates="art_id")

    def __repr__(self):
        return f'<Positive_news article_id={self.article_id}>'



def connect_to_db(flask_app, db_uri="postgresql:///reminders", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
