from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO, send, emit

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = 'secret!'
socket = SocketIO(app)

app.config.from_object('config')
try:
    # try to load config from instance directory
    app.config.from_pyfile('config.py')
except FileNotFoundError:
    print('instance/config.py does not exist')


db = SQLAlchemy(app)
migrate = Migrate(app, db)
from .models import *

from .views.api_1 import api_1
from .views.api_2 import api_2
app.register_blueprint(api_1, url_prefix = '/api/1')
app.register_blueprint(api_2, url_prefix = '/api/2')

@app.route('/')
def index():
    return 'Hello!'

if __name__ == '__main__':
    socket.run(app)
