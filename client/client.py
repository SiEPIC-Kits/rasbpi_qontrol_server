# import socket
# hostip = 'localhost'
# hostport = 8089
#
# class client_qontrol():
#     def __init__(self):
#         clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         clientsocket.connect((hostip, hostport))
#         clientsocket.send(bytes('Client Connected.', 'UTF-8'))
#         self.do()
#
#     def recognized_command(self,command):
#         clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         clientsocket.connect((hostip, hostport))
#         clientsocket.send(bytes(command, 'UTF-8'))
#         response = clientsocket.recv(1024)
#         print(response.decode("UTF-8"))
#         return response.decode("UTF-8")
#
#     def do(self):
#         while True:
#             commandRAW = input('[Client]: ')
#             command = commandRAW.split()[0]
#
#             if command == 'help':
#                 print("Possible Commands: help, setvoltage, setcurrent, getvoltage, getcurrent.")
#                 continue
#             elif command == 'test_command' \
#             or command == 'setvoltage'\
#             or command == 'getvoltage'\
#             or command == 'setcurrent'\
#             or command == 'getcurrent'\
#             :
#                 self.recognized_command(commandRAW)
#
#             elif command == 'exit':
#                 print("Exited.")
#                 break
#             else:
#                 print("Command Not Recognized. Try: help")
#                 continue
#
#
#
# #x = client_qontrol()
# #recognized_command('test_command')

import socket
import select
import sys, os
from contextlib import contextmanager

hostip = 'localhost'
hostport = 8089

def connect(hostip=hostip,hostport=hostport):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP_address = hostip
    Port = hostport
    server.connect((IP_address, Port))
    #message = socks.recv(2048)
    #print("[Server]: "+message.decode("UTF-8"))
    return server

def terminal_mode():
    server = connect()
    server.send(bytes('Connected via Terminal. Hello!\n','UTF-8'))

    while True:
        # maintains a list of possible input streams
        sockets_list = [sys.stdin, server]
        """ There are two possible input situations. Either the
        user wants to give  manual input to send to other people,
        or the server is sending a message  to be printed on the
        screen. Select returns from sockets_list, the stream that
        is reader for input. So for example, if the server wants
        to send a message, then the if condition will hold true
        below.If the user wants to send a message, the else
        condition will evaluate as true"""
        read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

        for socks in read_sockets:
            if socks == server:
                message = socks.recv(2048)
                sys.stdout.write("[Server]: "+message.decode("UTF-8"))
                sys.stdout.write("\n\n[You]: ")
                sys.stdout.flush()
            else:
                message = sys.stdin.readline()
                if message == 'exit':
                    return
                else:
                    server.send(bytes(message, 'UTF-8'))

    print('Connection Closed.')
    server.close()

def send_command(message):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((hostip, hostport))
    clientsocket.recv(2048)#supress welcome message
    clientsocket.send(bytes(message, 'UTF-8'))
    response = clientsocket.recv(2048)
    clientsocket.close()
    #print(response.decode("UTF-8"))
    return response.decode("UTF-8")

try:
    if str(sys.argv[1]) == 'terminal':
        terminal_mode()
except:
    pass
