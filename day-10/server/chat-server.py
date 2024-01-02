import socketio  # pip install python-socketio
import eventlet  # pip install eventlet

sio = socketio.Server()


@sio.event
def connect(sid, environ):
    print(f"Client {sid} connected")


@sio.event
def disconnect(sid):
    print(f"Client {sid} disconnected")


@sio.event
def chat_message(sid, data):
    print(f"Message from {sid}: {data}")
    sio.emit('message', data)


@sio.event
def chat_join(sid, data):
    print(f"Join {sid}: {data}")
    sio.emit('join', data)


if __name__ == '__main__':
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)
