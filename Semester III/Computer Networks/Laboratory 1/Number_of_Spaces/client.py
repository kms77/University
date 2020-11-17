import socket
# Create a TCP/IP socket
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 2764)
Socket.connect(server_address)
try:
    amount_received = 0
    amount_expected = 2048
    while True:
        # Give the input string
        given_string = input("Give an input: ")
        # Validation step
        if not given_string:
            print("Not a valid input!")
            break
        data_to_send = str(given_string)
        # Send data to the server
        Socket.sendall(bytes(data_to_send, 'utf-8'))
        print("String sent!")
        data = Socket.recv(amount_expected)
        amount_received += len(data)
        number_of_spaces = int(str(data.decode('utf-8')))
        # Print the result
        print("Number of spaces: " + str(number_of_spaces))
        break
finally:
    # Close the connection
    print("Socket closed!")
    Socket.close()
