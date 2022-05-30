import socket
s = socket.socket()

port = 12344
mssg ='Message from client!'
s.connect(('127.0.0.1', port))
s.sendto(mssg.encode(),('127.0.0.1', port))
print("Server message ", s.recv(1024).decode())
s.close()