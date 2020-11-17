import socket
import json
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 2764)
sock.connect(server_address)
try:
    amount_received = 0
    amount_expected = 2048
    array = []
    while True:
        # Give the number of elements in the array
        number_of_elements = int(input("Choose the size of the array: "))
        if number_of_elements <= 0:
            print("Invalid input!\n")
            message_to_sent = 'Quit'
            break
        while number_of_elements > 0:
            # Get a new input number
            number = int(input('Number: '))
            array.append(number)
            number_of_elements = number_of_elements - 1
        data_to_send = json.dumps({"a": array})
        # Send data to the server
        sock.sendall(data_to_send.encode())
        print("Array was sent!")
        data = sock.recv(amount_expected)
        amount_received += len(data)
        sum_of_elements = int(str(data.decode("utf-8")))
        # Print the result
        print("Sum of elements: " + str(sum_of_elements))
        break
finally:
    # Close the connection
    print("Socket closed!")
    sock.close()
