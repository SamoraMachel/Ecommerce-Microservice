from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

def get_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABSE_URL")
    return app

def get_db()-> SQLAlchemy:
    db = SQLAlchemy(get_app())
    return db