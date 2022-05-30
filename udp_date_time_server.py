import socket
import datetime
localt = datetime.datetime.now()
stime = str(localt)
# ltime = bytes(localt)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # For UDP ,by default (Socket_family and Socket_type) is TCP
udp_host = socket.gethostname()		        # Host IP
udp_port = 12345			                # specified port to connect

msg = 'Hello this is UDP server'
sock.bind((udp_host,udp_port))

while True:
    print ("Waiting for client...")
    data,addr = sock.recvfrom(1024)	        #receive data from client
    print ("Received Messages:",data.decode()," from",addr)
    sock.sendto(stime.encode(),addr)
    print("\n Listened!! Closing Connection .... ")
    break