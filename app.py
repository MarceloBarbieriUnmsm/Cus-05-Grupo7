import psycopg2
from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from utils.db import db

app = Flask(__name__)

app.secret_key= "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://modulo4:modulo4@137.184.120.127:5432/sigcon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(contacts)


