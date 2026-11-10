import socket
import json
def find_type(m):
    n = len(m)
    upper = True
    lower = True
    for i in range(n):
        for j in range(n):
            if i > j and m[i][j] != 0:
                upper = False
            if i < j and m[i][j] != 0:
                lower = False
    if upper and lower:
        return "Diagonal"
    elif upper:
        return "upper"
    elif lower:
        return "lower"
    else:
        return "neither"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",5000))
server.listen(1)
print("server is listening...")
conn, addr = server.accept()
data = b""
while True:
    chunk = conn.recv(4096)
    if not chunk:
        break
    data += chunk
matrix = json.loads(data.decode())
result = find_type(matrix)
print("result:",result)
conn.send(result.encode())
conn.close()
server.close()