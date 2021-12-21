import socket
import os
import sys
from time import sleep
from threading import Thread
try:
    from config import IP, PORT
except:
    print("No config file found, please create one. (.py format)")
    print("Formate should be as follows:")
    print("IP = ip-here'")
    print("PORT = port-here")
    sys.exit(1)

if sys.platform == 'win32':
    clear = 'cls'
else:
    clear = 'clear'

os.system(clear)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((IP, int(PORT)))
    print("Connected to server")
except:
    print("Connection failed")
    exit()

def recv():
    while True:
        try:
            recvdata = client_socket.recv(512)
        except:
            sys.exit()
        if not recvdata:
            print("Server disconnected")
            client_socket.close()
            sys.exit()
        if recvdata.decode().lower() == 'clear':
            os.system(clear)
        else:
            print(recvdata.decode())
        
def send():
    while True:
        sleep(0.0001)     
        send_data = input('->')
        if send_data == "":
            pass
        elif send_data.lower() == 'exit':
            client_socket.send(send_data.encode())
            client_socket.close()
            sys.exit()
        else:
            try:
                client_socket.send(send_data.encode())
            except:
                print("Couldn't send :(")
                client_socket.close()
                sys.exit()

Thread(target=recv).start()
sleep(0.2)
Thread(target=send).start()
