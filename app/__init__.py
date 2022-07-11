from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(db)

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app