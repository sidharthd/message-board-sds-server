from flask import Blueprint, request
import json

api_2 = Blueprint('api_v2', __name__)

from .. import db, socket
from ..models import Tweet, Comment

@api_2.route('/')
def test():
    return 'API 2'

@api_2.route('/post-tweet/', methods=['POST'])
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
