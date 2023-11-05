import socket
import subprocess
UDP_IP = 'localhost'
UDP_port = 8080
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_port))
while True:
    data,addr = sock.recvfrom(1024)
    str_ = data.decode('utf-8')
    print("Connected by:",addr)
    print("message:",str_)
    print('Opening:',str_)
    subprocess.call(str_)

