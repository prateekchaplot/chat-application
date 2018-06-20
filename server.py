import socket, threading

class Server:
    connections = []

    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 10000))

        sock.listen(1)
        print('Server Running...')
    
        while True:
            conn, addr = sock.accept()
            
            cThread = threading.Thread(target=self.handler, args=(conn, addr))
            cThread.daemon = True
            cThread.start()

            self.connections.append(conn)
            print(str(addr[0]) + ':' + str(addr[1]), 'connected')


    def handler(self, conn, addr):
        pass

server = Server()