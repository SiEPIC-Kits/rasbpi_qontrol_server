##
#Author: Stephen
##

#https://stackoverflow.com/questions/7749341/basic-python-client-socket-example
import socket
import select
from _thread import *
import sys

import siepicQontrol
from time import gmtime, strftime

host = 'localhost'
port = 8089

serverqontrol = siepicQontrol.siepicqontrol()
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host, port))
serversocket.listen(5) # become a server socket, maximum 5 connections
list_of_clients = []
print("SiEPIC_Qontrol Server Online.")

#Connect to Qontrol Unit
try:
    q=serverqontrol.connect()
    print('Connected to Qontrol.\n')
except:
    print('Could not connect to Qontrol')


def clientthread(conn, addr):
    # sends a message to the client whose user object is conn
    #conn.send(bytes("Connected to SiEPIC-Qontrol!", 'UTF-8'))
    while True:
        try:
            message = conn.recv(2048).decode("UTF-8")
            if message:
                """prints the message and address of the
                user who just sent the message on the server
                terminal"""
                #print("[" + addr[0] + "]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"]: " + message)
                sys.stdout.write("[" + addr[0] + "]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"]: " + message)
                sys.stdout.flush()

                #parse Commands
                message = message.split()
                #Commands here
                #TEST
                if message[0] == 'test_command':
                    data = serverqontrol.test_command()
                    print(data)
                #SET
                elif message[0] == 'setvoltage':
                    if len(message)==3:
                        chan = int(message[1])
                        voltage = float(message[2])
                        data = serverqontrol.set_voltage(q,chan,voltage)
                    else:
                        data='setvoltage parameters incorrect.'
                    print(data)
                elif message[0] == 'setcurrent':
                    if len(message)==3:
                        chan = int(message[1])
                        current = float(message[2])
                        data = serverqontrol.set_current(q,chan,current)
                    else:
                        data='setcurrent parameters incorrect.'
                    print(data)
                #GET
                elif message[0] == 'getvoltage':
                    if len(message)==2:
                        chan = int(message[1])
                    else:
                        data='getvoltage parameters incorrect.'
                    data = serverqontrol.get_voltage(q,chan)
                    print(data)
                elif message[0] == 'getcurrent':
                    if len(message)==2:
                        chan = int(message[1])
                    else:
                        data='getcurrent parameters incorrect.'
                    data = serverqontrol.get_current(q,chan)
                    print(data)

                #RESET
                elif message[0] == 'resetvoltage':
                    if len(message)==2:
                        chan = int(message[1])
                    else:
                        data='resetvoltage parameters incorrect.'
                    data = serverqontrol.reset_voltage(q,chan)
                    print(data)
                elif message[0] == 'resetcurrent':
                    if len(message)==2:
                        chan = int(message[1])
                    else:
                        data='resetcurrent parameters incorrect.'
                    data = serverqontrol.reset_current(q,chan)
                    print(data)

                elif message[0] == 'resetvoltageall':
                    data = serverqontrol.reset_voltage_all(q)
                    print(data)
                elif message[0] == 'resetcurrentall':
                    data = serverqontrol.reset_current_all(q)
                    print(data)

                elif message[0] == 'resetvoltagerange':
                    if len(message)==3:
                        chan = int(message[1])
                        chan2 = int(message[2])
                    else:
                        data='resetvoltagerange parameters incorrect.'
                    data = serverqontrol.reset_voltage_range(q,chan,chan2)
                    print(data)
                elif message[0] == 'resetcurrentrange':
                    if len(message)==3:
                        chan = int(message[1])
                        chan2= int(message[2])
                    else:
                        data='resetcurrentrange parameters incorrect.'
                    data = serverqontrol.reset_current_range(q,chan,chan2)
                    print(data)

                elif message[-1] == 'Hello!':
                    data = "Connected to SiEPIC-Qontrol!"

                elif message[0] == 'help':
                    if len(message)>1:
                        if message[1] == 'test_command':
                            data='A simple call and response to the server.'
                        elif message[1] == 'exit':
                            data='Exits terminal mode.'
                        elif message[1] == 'setvoltage':
                            data='Sets the voltage of the control unit for a certain channel in VOLTS.\nusage: setvoltage CHANNEL VOLTAGE.'
                        elif message[1] == 'setcurrent':
                            data='Sets the current of the control unit for a certain channel in AMPS.\nusage: setcurrent CHANNEL CURRENT.'
                        elif message[1] == 'getvoltage':
                            data='Gets the voltage of the control unit for a certain channel in VOLTS.\nusage: getvoltage CHANNEL.'
                        elif message[1] == 'getcurrent':
                            data='Gets the current of the control unit for a certain channel in AMPS.\nusage: getcurrent CHANNEL.'
                        elif message[1] == 'resetvoltage':
                            data='Resets the voltage of the control unit for a certain channel to 0 VOLTS.\nusage: resetvoltage CHANNEL.'
                        elif message[1] == 'resetcurrent':
                            data='Resets the current of the control unit for a certain channel to 0 AMPS.\nusage: resetcurrent CHANNEL.'
                        elif message[1] == 'resetvoltageall':
                            data='Resets the voltage of the control unit for all channels to 0 VOLTS.\nusage: resetvoltageall.'
                        elif message[1] == 'resetcurrentall':
                            data='Resets the current of the control unit for all channels to 0 AMPS.\nusage: resetcurrentall.'
                        elif message[1] == 'resetvoltagerange':
                            data='Resets the voltage of the control unit for a range of channels to 0 VOLTS.\nusage: resetvoltagerange CHANNEL1 CHANNEL2.'
                        elif message[1] == 'resetcurrentrange':
                            data='Resets the current of the control unit for a range of channels to 0 AMPS.\nusage: resetcurrentrange CHANNEL1 CHANNEL2.'
                        else:
                            data = 'Command Not Recognized. Try \'help\''
                    else:
                        data='Possible Suffix: test_command, setvoltage, setcurrent, getvoltage, getcurrent, resetvoltage, resetcurrent, resetvoltageall, resetcurrentall, resetvoltagerange, resetcurrentrange exit.\nusage: help test_command.'
                    print('Help invoked.')
                else:
                    data = 'Command Not Recognized. Try \'help\''
                broadcast(data, conn)

            else:
                """message may have no content if the connection
                is broken, in this case we remove the connection"""
                remove(conn)
        except:
            continue

"""Using the below function, we broadcast the message to all
clients who's object is not the same as the one sending
the message """
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients==connection:
            try:
                clients.send(bytes(message, 'UTF-8'))
            except:
                clients.close()
                # if the link is broken, we remove the client
                remove(clients)

"""The following function simply removes the object
from the list that was created at the beginning of
the program"""
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    """Accepts a connection request and stores two parameters,
    conn which is a socket object for that user, and addr
    which contains the IP address of the client that just
    connected"""
    conn, addr = serversocket.accept()
    """Maintains a list of clients for ease of broadcasting
    a message to all available people in the chatroom"""
    list_of_clients.append(conn)
    # prints the address of the user that just connected
    #print(addr[0] + " connected.")
    # creates and individual thread for every user
    # that connects
    start_new_thread(clientthread,(conn,addr))

conn.close()
server.close()
