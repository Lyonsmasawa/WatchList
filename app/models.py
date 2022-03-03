from enum import unique
from importlib_metadata import email
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class Movie:
    
    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count

class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    movie_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(movie_id=id).all()
        return reviews
    # def save_review(self):
    #     Review.all_reviews.append(self)


    # @classmethod
    # def clear_reviews(cls):
    #     Review.all_reviews.clear()

    # @classmethod
    # def get_reviews(cls,id):

    #     response = []

    #     for review in cls.all_reviews:
    #         if review.movie_id == id:
    #             response.append(review)

    #     return response

class User(UserMixin, db.Model): #arg helps connect  to db
    __tablename__ = 'users' #table name
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) #tels alchemy foreign key and is the primary key of roles
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

    @property #create write only class property password
    def password(self):
        raise AttributeError('You cannot read the password attribute') #we raise an attribute error to block access to the password property

    @password.setter
    def password(self, password):  #save hash to pass_secure column in database
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self, password): #takes pass hashes it and checks if it is the same
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy="dynamic")
    """
    the db.relationship creates a virtual column
    """

    def __repr__(self):
        return f'Role {self.name}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))