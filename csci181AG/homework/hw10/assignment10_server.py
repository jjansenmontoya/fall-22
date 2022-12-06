import socket

HOST = "127.0.0.1"
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()
while True: 
    conn, addr = s.accept()
    recievedMessage = conn.recv(4096).decode()
    try:
        requestedFile = recievedMessage[5:15]
        file = open(requestedFile,"r")
        contents = file.read()
        file.close()
        initialLine = "HTTP/1.1 200 OK\n"
        secondLines = "Content-Type:text/html\nConnection:close\n\n"
        message = initialLine + secondLines + contents
    except:
        initialLine = "HTTP/1.1 404 Not Found\n"
        secondLines = "Content-Type:text/html\nConnection:close\n\n"
        message = initialLine + secondLines + "failure"
    conn.sendall(message.encode())
s.close()