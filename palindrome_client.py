import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
n = input("Enter the string:")
client.connect(("127.0.0.1",8000))
client.send(n.encode())

result = client.recv(1024).decode()
print("result is:",result)
client.close()