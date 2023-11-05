import socket
def client_p():
    host  = socket.gethostname()
    port = 5000
    s = socket.socket()
    s.connect((host,port))
    print("Type bye to terminate!!!")
    data = input('->')
    while data.lower().strip() != 'bye':
        s.send(data.encode())
        data = s.recv(1024).decode()
        print("Message from server:" + str(data))
        data = input('->')
    s.close()  

if __name__ == '__main__':
    client_p()      