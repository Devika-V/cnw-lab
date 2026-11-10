import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",7000))
server.listen(1)
print("server listening...")
conn, addr = server.accept()
data = conn.recv(1024).decode()
a,b = map(int,data.split())
def sum(a,b):
    result = a+b
    return result
conn.send(str(sum(a,b)).encode())
conn.close()
server.close()