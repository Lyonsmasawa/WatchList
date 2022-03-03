from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Movie:
    
    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count

class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response

class User(db.Model): #arg helps connect  to db
    __tablename__ = 'users' #table name
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) #tels alchemy foreign key and is the primary key of roles

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