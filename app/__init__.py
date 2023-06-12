from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

db = SQLAlchemy()
api = Api()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key'
    app.config['JWT_SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # Register Todo App

    from app.path import TODO_API_PATH, AUTH_API_PATH

    TODO_API_PATH()

    # Register Auth App

    AUTH_API_PATH()

    api.init_app(app)

    jwt = JWTManager(app)
    Migrate(app, db)

    return app