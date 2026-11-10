import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
client.connect(("127.0.0.1",7000))
client.send(f"{a} {b}".encode())
result = client.recv(1024).decode()
print("sum of a and b is:",result)
client.close()