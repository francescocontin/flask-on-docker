import os

from werkzeug.utils import secure_filename
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    redirect,
    url_for,
    render_template
)
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_socketio import send, emit

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route("/")
def hello_world():
    return render_template('index.html')

@socketio.on('connected')
def test_connect(data):
    print('Client connect')
    send(data)


if __name__ == '__main__':
    socketio.run(app)
