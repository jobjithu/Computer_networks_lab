import socket
def server_p():
    host = socket.gethostname()
    port = 5000
    s = socket.socket()
    s.bind((host,port))
    s.listen(2)
    conn,addr = s.accept()
    print("Connected by:",addr)
    while True:
        data = conn.recv(1024).decode()
        if not data:break
        print("Message from client:" + str(data))
        data = input('->')
        conn.send(data.encode())
    conn.close()    

if __name__ == '__main__':
    server_p()    