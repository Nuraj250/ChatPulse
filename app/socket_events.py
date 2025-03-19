from flask_socketio import emit, join_room, leave_room
from app import socketio

def generate_avatar(username):
    """Generate a unique avatar using Gravatar."""
    hash_email = hashlib.md5(username.encode()).hexdigest()
    return f"https://www.gravatar.com/avatar/{hash_email}?d=identicon"

@socketio.on("connect")
def handle_connect():
    print("A user connected")

@socketio.on("disconnect")
def handle_disconnect():
    print("A user disconnected")

@socketio.on("send_message")
def handle_message(data):
    emit("receive_message", data, broadcast=True)
