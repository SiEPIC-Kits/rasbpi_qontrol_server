import socket
hostip = 'localhost'
hostport = 8089

class client_qontrol():
    def __init__(self):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((hostip, hostport))
        clientsocket.send(bytes('Client Connected.', 'UTF-8'))
        self.do()

    def recognized_command(self,command):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((hostip, hostport))
        clientsocket.send(bytes(command, 'UTF-8'))
        response = clientsocket.recv(1024)
        print(response.decode("UTF-8"))
        return response.decode("UTF-8")

    def do(self):
        while True:
            commandRAW = input('[Client]: ')
            command = commandRAW.split()[0]

            if command == 'help':
                print("Possible Commands: help, setvoltage, setcurrent, getvoltage, getcurrent.")
                continue
            elif command == 'test_command' \
            or command == 'setvoltage'\
            or command == 'getvoltage'\
            or command == 'setcurrent'\
            or command == 'getcurrent'\
            :
                self.recognized_command(commandRAW)

            elif command == 'exit':
                print("Exited.")
                break
            else:
                print("Command Not Recognized. Try: help")
                continue



#x = client_qontrol()
#recognized_command('test_command')
