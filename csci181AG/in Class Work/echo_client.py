import socket

HOST = "127.0.0.1"
PORT = 65431

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
inputClient = input("Please type your name: ")
s.sendall(inputClient.encode())
name = s.recv(1024).decode()
while True:
    inputClient = input("Chat: ")
    s.sendall(inputClient.encode())
    if inputClient.lower() == "bye":
        break
    data = s.recv(1024).decode()
    print(name + ": " + data)
s.close()