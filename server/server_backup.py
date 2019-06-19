#https://stackoverflow.com/questions/7749341/basic-python-client-socket-example
import socket
import siepicQontrol
from time import gmtime, strftime
import threading

host = 'localhost'
port = 8089

class server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        serverqontrol = siepicQontrol.siepicqontrol()
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((host, port))
        serversocket.listen(5) # become a server socket, maximum 5 connections

        #Connect to Qontrol Unit
        # try:
        #     serverqontrol.connect()
        # except:
        #     print('Could not connect to Qontrol')
        #     break

        #Idle Server
        print('Rasbpi Server Online')
        while True:
            #Here, you have the client connection for replies
            connection, address = serversocket.accept()
            buf = connection.recv(64) #buf is the client input
            if len(buf) > 0:
                data = None
                client_input = buf.decode("UTF-8")
                print("[client]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+client_input)

                #parse Commands
                client_input = client_input.split()
                #Commands here
                #TEST
                if client_input[0] == 'test_command':
                    data = serverqontrol.test_command()
                #SET
                elif client_input[0] == 'setvoltage':
                    print('TEMP')

                elif client_input[0] == 'setcurrent':
                    print('TEMP')
                #GET
                elif client_input[0] == 'getvoltage':
                    print('TEMP')

                elif client_input[0] == 'getcurrent':
                    print('TEMP')

                #Clear the dat aafter sending the results to the client
                if data!=None:
                    #data = bytes(data, 'UTF-8')
                    #connection.sendall(data)
                    connection.send(bytes(data, 'UTF-8'))
                    data = None
                else:
                    data='Complete.'
                    connection.send(bytes(data, 'UTF-8'))
                    data = None

class localcommand(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        while True:
            if input('[Server]: Type exit to close server: ') == 'exit':
                print('Server Shutdown.')
                serversocket.shutdown(socket.SHUT_RDWR)
                serversocket.close()
                break

thread1 = server()
#thread2 = localcommand()
try:
    thread1.start()
    #thread2.start()
except:
    print('Could not start server.')
# try:
#    thread.start_new_thread(server_commands())
#    thread.start_new_thread(start_server())
# except:
#    print("Error: unable to start thread.")
