import sqlalchemy
from app import get_db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db : SQLAlchemy = get_db()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=datetime.utcnow())
    
    def __repr__(self) -> str:
        return f'<User {self.first_name} - {self.last_name}>'
    