import socket
host = '127.0.0.1'
port = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn,addr = s.accept()
print("Connected by:",addr)
while True:
    data = conn.recv(1024)
    print(data)
    if not data : break
    conn.send(data)
conn.close()    