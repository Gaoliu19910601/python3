'''User Datagram Protocol (UDP connection [unreliable])'''

import socket

def Main():
    host = "127.0.0.1"

    port = 5001

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    server = ("127.0.0.1",5000)

    s.bind((host,port))

    message = input("->")

    while message != 'q':
        s.sendto(message.encode('utf-8'),server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('Recieved from server: ' + data)
        message = input('->')
    s.close()

if __name__ == "__main__":
    Main()
