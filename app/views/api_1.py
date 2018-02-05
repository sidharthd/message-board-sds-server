from flask import Blueprint, request
import json
import re
from sqlalchemy.exc import IntegrityError

api_1 = Blueprint('api_v1', __name__)

from .. import db, socket, bcrypt
from ..models import Tweet, Comment, Account

@api_1.route('/')
def index():
    return 'API 1'

@api_1.route('/login/', methods = ['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    hash = bcrypt.generate_password_hash(password).decode('utf-8')
    account = Account.query.filter_by(email = email).first()
    if account:
        if bcrypt.check_password_hash(account.password, password):
            return json.dumps({'result' : 'success'})
        else:
            return json.dumps({'result' : 'failure'})
    else:
        return json.dumps({'result' : 'failure'})

@api_1.route('/signup/', methods = ['POST'])
def signup():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    hash = bcrypt.generate_password_hash(password).decode('utf-8')
    try:
        account = Account(
            name = name,
            email = email,
            password = hash
        )
        db.session.add(account)
        db.session.commit()
    except IntegrityError:
        return json.dumps({
            'result': 'failure',
            'error': 'email'
        })
    return json.dumps({'result' : 'success'})

@api_1.route('/tweets/')
def getTweets():
    tweets = [
        {
            'key': tweet.id,
            'tweet': tweet.tweet,
            'author': tweet.author
        }
        for tweet in Tweet.query.all()
    ]
    return json.dumps({'tweets': tweets})

@api_1.route('/tweet/<int:tweetId>')
def getTweet(tweetId):
    return 'JSON of tweet and comments'

@api_1.route('/post-tweet/', methods=['POST'])
def newTweet():
    tweet = request.json['tweet']

    # check if author field exists or if author field is undefined
    if not request.json.get('author') or request.json['author'] == 'undefined' :
        author = 'Anonymous'
    else:
        author = request.json['author']

        # remove leading, trailing, and continous whitespaces
        author = " ".join(author.split())

        if author == '':
            author = 'Anonymous'

    # create a database record object
    _tweet = Tweet(tweet, author)
    db.session.add(_tweet)
    db.session.commit()

    # create a dictionary to be broadcasted to all connected clients
    tweet = {
        'key': _tweet.id,
        'tweet': _tweet.tweet,
        'author': _tweet.author
    }

    socket.emit('new tweet', tweet, broadcast = True)
    return json.dumps({'tweet': tweet})
