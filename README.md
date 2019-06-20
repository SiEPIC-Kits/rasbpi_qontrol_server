# rasbpi_qontrol_server

A simple library for a remote server connected to a Qontrol unit. Clients can connect in two ways, terminal-mode or command-mode, and make calls to the server for the Qontrol unit. The server will respond the result as a string. Terminal-mode keeps an open connection and responses are returned in a sentence structure for readability/demos. Command-mode will open a connection that sends a single command and waiting for the response, then closes the connection. The responses for command mode are returned as their float values.

The server allows up to 5 connections at once, this might effect the usage of the Qontrol unit, please adjust to your own needs.

## Prerequisites
* Python 3
* Linux Machine
* Non-super user USB Access (see below) - SERVER ONLY

`server.py` does not work properly when invoked using `sudo`. Thus, the server machine needs access to the USB ports without the need of sudo. Here is the fix used during testing:
```
create /etc/udev/rules.d/01-ttyusb.rules
contents: SUBSYSTEMS=="usb-serial", TAG+="uaccess"
sudo udevadm control --reload, to reload
```

## How to Start
### Server
```
python server.py
```
### Client
Terminal Mode:
```
python client.py terminal
```
or
```
python client.py terminal windows
```
for Windows users.

Command-mode:
Simply import the client.py as a class, establish a link to the server using `connect(IP,PORT)`, then start sending single commands using `send_command('test_command')`.
```
import client.py
connect(localhost,8089)
send_command('Hello!')
```

## Client Commands
* help
* setvoltage
* setcurrent
* getvoltage
* getcurrent
* resetvoltage
* resetcurrent
* resetvoltagerange
* resetcurrentrange
* resetvoltageall
* resetcurrentall
* exit

## Acknowledgements
* [Qontrol Python API](http://qontrol.co.uk/getting-started-with-the-python-api/)
* [Basic Python Socket Chatroom](https://www.geeksforgeeks.org/simple-chat-room-using-python/)
* [USB Permissions for Linux](https://arduino.stackexchange.com/questions/21215/first-time-set-up-permission-denied-to-usb-port-ubuntu-14-04)
