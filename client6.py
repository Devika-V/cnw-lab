import socket
client =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sentence = input("Enter the sentence:")
client.sendto(sentence.encode(),("127.0.0.1",6000))
reply,addr = client.recvfrom(1094)
print("formal english:",reply.decode())
client.close()