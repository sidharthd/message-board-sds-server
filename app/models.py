from . import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

class Account(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(50), nullable = False, unique = True)
    password = db.Column(db.String(128), nullable = False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tweet = db.Column(db.String(140), nullable = False)
    author = db.Column(db.String(20), nullable = False)
    comments = db.relationship('Comment', backref = 'tweet', lazy = True)

    def __init__(self, tweet, author):
        self.tweet = tweet
        self.author = author

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(140), nullable = False)
    tweet_id = db.Column(db.Integer, db.ForeignKey('tweet.id'), nullable = False)

    def __init__(self, comment, tweet_id):
        self.comment = tweet
        self.tweet_id = tweet_id
