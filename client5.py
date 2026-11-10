import socket
import json
import random

n = int(input("Enter the value for n:"))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(1,50))
    matrix.append(row)
for row in matrix:
    print(row)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",5000))
client.sendall(json.dumps(matrix).encode())
client.shutdown(socket.SHUT_WR)
reply = client.recv(1024).decode()
print("Server says:",reply)
client.close()
