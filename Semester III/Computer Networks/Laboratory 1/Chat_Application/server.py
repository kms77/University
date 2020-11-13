import socket
import sys

# Create a TCP/IP socket
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 2764)
print('Starting up on ' + str(sys.stderr) + 'port %s' + str(server_address))
Socket.bind(server_address)
# It specifies the number of unaccepted connections that the system will allow before refusing new connections
Socket.listen(0)
while True:
    print('Waiting for a connection...')
    connection, client_address = Socket.accept()
    print("Socket accepted!")
    try:
        print('Connection from: ', client_address)
        data = connection.recv(1024)
        # first message from the client(the one who starts the conversation)
        print('Client: ' + str(data.decode('utf-8')))
        while True:
            client_input = str(data.decode('utf-8'))
            # close condition
            if client_input == 'Quit':
                break
            server_input = input("Server: ")
            message_to_sent = str(server_input)
            # send message to client
            connection.sendall(bytes(message_to_sent, 'utf-8'))
            # close condition
            if server_input == 'Quit':
                break
            # receive message from client
            data = connection.recv(1024)
            print('Client: ' + str(data.decode('utf-8')))
    finally:
        connection.close()
        print("Connection closed!")
