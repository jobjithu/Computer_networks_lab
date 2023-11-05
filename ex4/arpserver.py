import socket
UDP_IP = 'localhost'
UDP_port = 8080
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_port))
ip = ['172.0.0.1','142.0.0.1']
mac = ['C1:0A:11:CB','C2:90:20:CD']
while True:
    data,addr = sock.recvfrom(1024)
    str_ = data.decode('utf-8')
    l = len(str_)
    if l != 0:
        print("Message received:",str_)
    break         
for x in ip:
    if str_ in x:
        ind = ip.index(str_)
        print("Mac address:",mac[ind])        