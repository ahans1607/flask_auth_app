from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

#invoke SQLALCHEMY so that it can be used later in our models and save it into a variable
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.urandom(24)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'

    db.init_app(app)

    #blueprint for auth routes in our app
    from ../auth import auth as auth_blueprint
