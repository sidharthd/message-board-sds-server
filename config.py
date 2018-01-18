import os

DEBUG = False

if os.environ.get('DATABASE_URL'):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SQLALCHEMY_TRACK_MODIFICATIONS = False
