import socket
import threading

header = 64
port = 5050
format = 'utf-8'
Disconnect_msg = '!Disconnect'
server = socket.gethostbyname(socket.gethostname())
# socket
address = (server, port)
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(address)

def handle_client(conn, addr):
    print(f'New connection{addr} connected.')

    connected = True
    while connected:
        msg_len = conn.recv(header).decode(format)
        if msg_len :
            msg_len = int(len(msg_len))
            msg = conn.recv(msg_len).decode(format)
            if msg == Disconnect_msg:
                connected = False
            print(f'[{addr}] {msg}')


# handle new connection
def start():
    SERVER.listen()
    print(f'Sever is listening on {server}!')
    while True:
        conn, addr = SERVER.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'Active connection with {threading.active_count()-1}')


print('Sever starts listening!')
start()