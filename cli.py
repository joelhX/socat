import socket
server=("192.168.219.108", 5678)
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.sendto(b"123", server)

#socat UDP-LISTEN:5678,fork UDP:192.168.219.101:4567
