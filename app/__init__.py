from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from run import get_app, get_db

app : Flask = get_app()
db : SQLAlchemy = get_db()

migrate = Migrate(app, db)