import socket 
s = socket.socket() #default TCP 
print("Socet Successfully created");

port = 12344

s.bind(('',port))
print("socket binded to %s" %(port))

s.listen(5)
print("Socket started listening")

while True:
    c, addr = s.accept()
    print('got connection from', addr);
    data,adr = c.recvfrom(1024)
    print(data.decode())
    c.send('End... Thanks for Connecting. '.encode())
    c.close()
    break

