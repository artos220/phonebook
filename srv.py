import socket
import select

def handle(c):
    data = c.recv(1024)
    if not data:
        connections.remove(c)
        c.close()
        return
    print(data)
    c.sendall(data)


s = socket.socket()
s.setblocking(False)
s.bind(('127.0.0.1', 5000))
s.listen(5)
connections = [s]
print("Waiting for connections")
try:
    while True:
        s_rs, _, _ = select.select(connections, [], [])
        for s_r in s_rs:
            if s_r == s:
                c, addr = s.accept()
                print("Connected", addr)
                connections.append(c)
            else:
                handle(s_r)
except KeyboardInterrupt:
    s.close()
