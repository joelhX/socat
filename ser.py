import socket
server=("192.168.219.101", 4567)
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind(server)
while(True): 
	buffer,sender = sock.recvfrom(1024*1024)
	print(sender,buffer.decode())
 

 #iptables -t nat -A PREROUTING -i [unicast-interface] -p udp --dport [unicast-incoming-port] -j DNAT --to-destination [multicast-addr]:[multicast-port]