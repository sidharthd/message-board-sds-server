from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
try:
    # try to load config from instance directory
    app.config.from_pyfile('config.py')
except app.config.from_pyfile('config.py'):
    print('instance/config.py does not exist')


db = SQLAlchemy(app)
migrate = Migrate(app, db)
from .models import *

from .views.api_1 import api_1
app.register_blueprint(api_1, url_prefix = '/api/1')

@app.route('/')
def index():
    return 'Hello!'
