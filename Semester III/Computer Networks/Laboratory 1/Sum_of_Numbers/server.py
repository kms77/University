import socket
import sys
import json
# Create a TCP/IP socket
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 2764)
print('Starting up on ' + str(sys.stderr) + 'port %s' + str(server_address))
Socket.bind(server_address)
# It specifies the number of unaccepted connections that the system will allow before refusing new connections
Socket.listen(2)
while True:
    print('Waiting for a connection...')
    connection, client_address = Socket.accept()
    print('Socket accepted!')
    try:
        print('Connection from: ', client_address)
        data = connection.recv(1024)
        # If we have a valid data
        if data:
            if data == 'Quit':
                print("Invalid input!\n")
                break
            data = json.loads(data.decode())
            print('Received: ' + str(data))
            array_of_received_numbers = data.get("a")
            if len(array_of_received_numbers) == 0:
                print("Empty array!\n")
                break
            sum_of_elements = 0
            for index in range(len(array_of_received_numbers)):
                sum_of_elements += array_of_received_numbers[index]
            result_to_send = str(sum_of_elements)
            connection.sendall(bytes(result_to_send, 'utf-8'))
        else:
            # If is not a valid data
            if not data:
                print("No data from %s." % client_address)
                break
    except Exception as exception:
        # If connection is not working
        localhost = '127.0.0.1'
        print("Something is wrong with the server %s and port %s. Exception is %s." % (
            localhost, server_address, exception))
    finally:
        # Close connection condition
        connection.close()
        print("Connection closed!")
