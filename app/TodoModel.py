from flask_login import UserMixin
from datetime import datetime
from app import db

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    task = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.String(100), nullable=False)