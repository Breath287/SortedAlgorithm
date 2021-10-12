import socket
import threading

header = 64
port = 5050
format = 'utf-8'
Disconnect_msg = '!Disconnect'
server = socket.gethostbyname(socket.gethostname())
# socket
address = (server, port)
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect(address)

def send(msg):
    message = msg.encode(format)
    msg_length = len(message)
    send_length = str(msg_length).encode(format)
    send_length += b' '*(header - len(send_length))
    CLIENT.send(send_length)
    CLIENT.send(message)


send('Hello, world!')
input()
send('nihao!')
input()
