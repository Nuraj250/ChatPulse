from flask_socketio import emit, join_room, leave_room
from app import socketio

@socketio.on("connect")
def handle_connect():
    print("A user connected")

@socketio.on("disconnect")
def handle_disconnect():
    print("A user disconnected")

@socketio.on("send_message")
def handle_message(data):
    emit("receive_message", data, broadcast=True)
