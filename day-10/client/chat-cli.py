import socketio  # pip install websocket-client

sio = socketio.Client()

intro = """
------------------------
        CHAT ROOM
------------------------"""


def main():
    print(intro)
    sio.connect('http://localhost:5000')

    name = input("> Enter your name: ")
    sio.emit('chat_join', {"name": name})

    while True:
        message = input("> Enter your message: ")
        sio.emit('chat_message', {"name": name, "message": message})


if __name__ == '__main__':
    main()
