import os
from flask import Flask
from flask_socketio import SocketIO
from config.settings import Config
from models.message import db

socketio = SocketIO()

def create_app():
    app = Flask(__name__, template_folder="../templates")  # Explicitly set template folder
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        
    from app.routes import main
    app.register_blueprint(main)

    socketio.init_app(app, cors_allowed_origins="*")
    
    return app
