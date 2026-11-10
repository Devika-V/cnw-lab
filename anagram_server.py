import socket 
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("127.0.0.1",8500))
data, addr = server.recvfrom(1024)
a,b = data.decode().split()
def anagram(a,b):
    l ={}
    if len(a) != len(b):
        return "not anagram"
    for i in a:
        l[i] = l.get(i,0) + 1
    for i in b:
        if i in l:
            l[i] -= 1
            if l[i] == 0:
                del(l[i])
        else:
            return "not anagram"
    if len(l) == 0:
        return "it is anagram"
    else:
        return "not anagram"

server.sendto(anagram(a,b).encode(),addr)
server.close()
