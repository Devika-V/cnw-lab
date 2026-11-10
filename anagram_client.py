import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
a = input("Enter string 1:")
b = input("Enter string 2:")
client.sendto(f"{a} {b}".encode(),("127.0.0.1",8500))
result,addr = client.recvfrom(1024)
ans = result.decode()
print("result is:",ans)
client.close()