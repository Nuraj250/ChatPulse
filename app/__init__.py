from flask import Flask
from flask_socketio import SocketIO
from config.settings import Config

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes import main
    app.register_blueprint(main)

    socketio.init_app(app, cors_allowed_origins="*")
    
    return app

