from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    avatar_url = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "username": self.username,
            "avatar_url": self.avatar_url,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%H:%M:%S")
        }
