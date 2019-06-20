# rasbpi_qontrol_server

A simple library for a remote server connected to a Qontrol unit. Clients can connect in two ways, terminal-mode or command-mode, and make calls to the server for the Qontrol unit. The server will respond the result as a string. Terminal-mode keeps an open connection and responses are returned in a sentence structure for readability/demos. Command-mode will open a connection that sends a single command and waiting for the response, then closes the connection. The responses for command mode are returned as their float values.

## Prerequisites
### Server
* TEMP
Tested on Linux: The server machine has to have access to the USB port connected to the Qontrol unit without the need of sudo.

### Client
* TEMP

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
* [Basic Python Socket Chatroom](https://www.geeksforgeeks.org/simple-chat-room-using-python/)
* [USB Permissions for Linux](https://arduino.stackexchange.com/questions/21215/first-time-set-up-permission-denied-to-usb-port-ubuntu-14-04)
