import select
import socket

HOST = '127.0.0.1'
PORT = 8890


class Connection:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr

    def receive(self):
        data = self.conn.recv(1024)
        if not data:
            self.conn.close()
        return data.decode()

    def send(self, data):
        self.conn.sendall(data.encode())

    def send_withnl(self, msg):
        self.send(f'{msg}\r\n')

    def input(self, msg):
        self.send_withnl(msg)
        return self.receive()

    def receive_input(self, message):
        return self.input(message).strip().upper()

    def close(self):
        self.conn.close()

    def handle(self, obj):
        data = self.conn.recv(1024)
        if not data:
            obj.connections.remove(self.conn)
            self.conn.close()
            return


class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.socket.bind((HOST, PORT))
        self.socket.listen(5)

    def stop(self):
        self.socket.close()

    def listen(self):
        conn, addr = self.socket.accept()
        return Connection(conn, addr)


# TODO need concurrency ???
class TelnetServer:
    def __init__(self):
        self.server = Server()
        self.server.start()
        self.conn = self.server.listen()
        self.connections = [self.server.socket]
        #self.select()

    def select(self):
        try:
            while True:
                s_rs, _, _ = select.select(self.connections, [], [])
                for s_r in s_rs:
                    if s_r == self.server.socket:
                        c, addr = self.server.socket.accept()
                        print("Connected", addr)
                        self.connections.append(c)
                        self.conn = Connection(c, addr)
                    else:
                        self.conn.handle(self)
                        # self.conn = s_r

        except KeyboardInterrupt:
            self.server.socket.close()

    def shutdown(self):
        self.conn.close()
        self.server.stop()
