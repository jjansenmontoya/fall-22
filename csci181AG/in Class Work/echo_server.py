import socket

HOST = "127.0.0.1"
PORT = 65431

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()
data = ""
while True: 
    conn, addr = s.accept()
    name = conn.recv(1024).decode()
    print('You are chatting with ' + name)
    conn.sendall(input("Please write your name: ").encode())
    while data.lower() != "bye":
        data = conn.recv(1024).decode()
        print(name + ": " + data)
        conn.sendall(input("Chat: ").encode())
s.close()