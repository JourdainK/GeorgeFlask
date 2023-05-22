from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'f7da476b4f7abcadd56d12d7f68a786b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://postgres:mons@localhost/george'

db = SQLAlchemy(app)

from . import routes
