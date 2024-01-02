import socketio  # pip install websocket-client

sio = socketio.Client()


@sio.event
def message(data):
    print(f"{data['name']}: {data['message']}")


@sio.event
def join(data):
    print(f"{data['name']} Joined")


if __name__ == '__main__':
    sio.connect('http://localhost:5000')
    sio.wait()
