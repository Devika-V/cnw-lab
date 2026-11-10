import socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("127.0.0.1",8900))
data, addr = server.recvfrom(1024)
s = data.decode()
def password(s):
    if len(s) == 8:
        return "Password is strong"
    return "Password not valid"
server.sendto(password(s).encode(),addr)
server.close()