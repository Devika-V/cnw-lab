import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",8000))
server.listen(1)
print("server is listening...")
conn, addr = server.accept()

data = conn.recv(1024).decode()

def palindrome(data):
    if data == data[::-1]:
        return "palindrome"
    return "not palindrome"
    

conn.send(palindrome(data).encode())
conn.close()
server.close()