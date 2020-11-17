import socket
import sys
# Create a TCP/IP socket
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 2764)
print('Starting up on ' + str(sys.stderr) + ' port %s' + str(server_address))
Socket.bind(server_address)
# It specifies the number of unaccepted connections that the system will allow before refusing new connections
Socket.listen(2)
while True:
    print('Waiting for a connection...')
    connection, client_address = Socket.accept()
    print('Socket accepted!')
    try:
        count = 0
        print('Connection from: ', client_address)
        data = connection.recv(1024)
        # If we have a valid data
        if data:
            given_string = str(data.decode("utf-8"))
            print("Received: " + str(given_string))
            for index in range(0, len(given_string)):
                if given_string[index] == " ":
                    count = count + 1
            data_to_send = str(count)
            connection.sendall(bytes(data_to_send, 'utf-8'))
            print("Number of spaces: " + str(count))
        else:
            # If it is not a valid data
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
