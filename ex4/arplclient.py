import socket
UDP_IP = 'localhost'
UDP_port = 8080
message  = '172.0.0.1'
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(bytes(message,'utf-8'),(UDP_IP,UDP_port))