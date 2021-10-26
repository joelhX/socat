import socket
import struct
server=("224.1.1.1", 4567)
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#mreq = socket.inet_aton("224.1.1.1") + socket.inet_aton("192.168.219.101")
mreq = struct.pack("4s4s", socket.inet_aton("224.1.1.1"),socket.inet_aton("192.168.219.101"))
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
sock.bind(("",4567))
while(True): 
	buffer,sender = sock.recvfrom(1024)
	print(sender,buffer.decode())
 