from flask import Blueprint, request
import json
import re

api_1 = Blueprint('api_v1', __name__)

from .. import db
from ..models import Tweet, Comment

@api_1.route('/')
def index():
    return 'API 1'

@api_1.route('/tweets/')
def getTweets():
    return 'JSON of all tweets'

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

    # tweet = request.json['tweet']
    # author = 'Anon'

    # create a database record object
    _tweet = Tweet(tweet, author)
    db.session.add(_tweet)
    db.session.commit()

    return json.dumps({'result': 'success'})
