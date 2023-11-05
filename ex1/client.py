import socket
host = '127.0.0.1'
port = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
str = 'Hello world!'
b = str.encode('utf-8')
s.send(b)
data = s.recv(1024)
print(data)
s.close()
