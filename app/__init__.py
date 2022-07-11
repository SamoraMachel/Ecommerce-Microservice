from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(db)

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.api.v1 import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')

    return app