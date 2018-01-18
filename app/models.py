from . import db

class Tweet(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    tweet = db.Column(db.String(140), nullable = False)
    author = db.Column(db.String(20), nullable = False)
    comments = db.relationship('Comment', backref = 'tweet', lazy = True)

    def __inti__(self, tweet, author):
        self.tweet = text
        self.author = author

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(140), nullable = False)
    tweet_id = db.Column(db.Integer, db.ForeignKey('tweet.id'), nullable = False)

    def __init__(self, comment, tweet_id):
        self.comment = text
        self.tweet_id = tweet_id
