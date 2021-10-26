import socket
mserver=("224.1.1.1", 5678)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL,32)
#sock.bind(("192.168.219.101",0))
b="1234567890"*1000
sock.sendto(b.encode(), mserver)

#socat UDP4-RECV:5678,ip-add-membership=224.1.1.1:192.168.219.108,reuseaddr UDP4-SENDTO:192.168.219.101:4567
#socat UDP4-RECVFROM:5678,ip-add-membership=224.1.1.1:192.168.219.108,fork UDP4-SENDTO:192.168.219.101:4567