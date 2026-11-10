import socket
abbr = {
    "tbh": "to be honest",
    "ig": "I guess",
    "tbf": "to be fair",
    "atm": "at the moment",
    "irl": "in real life",
    "lol": "laughing out loud",
    "asap": "as soon as possible",
    "omg": "oh my God",
    "ttyl": "talk to you later",
    "idk": "I don't know",
    "nvm": "never mind",
    "idc": "I don't care"
}
def translate(sentence):
    result = []
    words = sentence.split()
    for word in words:
        key = word.lower()
        if key in abbr:
            result .append(abbr[key])
        else:
            result.append(word)
    return " ".join(result)

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("127.0.0.1",6000))
print("server is listening...")
while True:
    data, addr = server.recvfrom(1024)
    sentence = data.decode()
    print("sentence is:",sentence)
    result = translate(sentence)
    server.sendto(result.encode(),addr)    
