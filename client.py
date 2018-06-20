import socket

class Client:
    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('127.0.0.1', 10000))

        print('Connected')

client = Client()