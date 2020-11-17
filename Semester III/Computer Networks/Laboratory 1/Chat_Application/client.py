import socket

# Create a TCP/IP
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 2764)
print('Connecting to ' + str(server_address))
Socket.connect(server_address)
try:
    amount_received = 0
    amount_expected = 2048
    while True:
        # client starts the conversation
        client_input = input("Client: ")
        # If it is an invalid input
        if not client_input:
            print("Invalid input!\n")
            message_to_send = 'Quit'
            Socket.sendall(bytes(message_to_send, 'utf-8'))
            break
        message_to_send = str(client_input)
        # send the message to server
        Socket.sendall(bytes(message_to_send, 'utf-8'))
        # close condition
        if str(client_input) == 'Quit':
            break
        # receive the message from server
        data = Socket.recv(amount_expected)
        print('Server: ' + str(data.decode('utf-8')))
        amount_received += len(data)
        # close condition
        if str(data.decode()) == 'Quit':
            break
finally:
    print("Connection closed!")
    Socket.close()
