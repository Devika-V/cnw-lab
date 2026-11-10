import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s = input("Enter password:")
client.sendto(s.encode(),("127.0.0.1",8900))
result,addr = client.recvfrom(1024)
print(result.decode())
client.close()