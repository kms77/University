import socket
import sys
import random

# Create a TCP/IP socket
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 2764)
print('Starting up on ' + str(sys.stderr) + 'port %s' + str(server_address))
Socket.bind(server_address)
# It specifies the number of unaccepted connections that the system will allow before refusing new connections
Socket.listen(2)
while True:
    # Wait for a connection str(sys.stderr) +
    print('Waiting for a connection...')
    connection, client_address = Socket.accept()
    print("Socket accepted!")
    # The data flow model is based on 3 chars:
    # first is the previous hit result
    # second one is the row we are going to attack
    # third is the collum we are going to attack
    stop_game = 1
    # Hard coded values
    board_game = [[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]
    try:
        print('Connection from: ', client_address)
        data = connection.recv(1024)
        print('Received: ' + str(data.decode('utf-8')))
        our_boats_number = 3
        number_of_enemy_boats = 3
        while True:
            enemy_hit = 0
            # We verify the received data: if we hit or not an enemy boat and if we got hit
            if str(data.decode("utf-8"))[0] == "1" or str(data.decode("utf-8"))[0] == "0":
                previous_hit = str(data.decode("utf-8"))
                result_hit = int(previous_hit[0])
                if result_hit == 1:
                    print("We hit enemy!")
                    number_of_enemy_boats = number_of_enemy_boats - 1
                if result_hit == 0:
                    print("We missed enemy!")
                if number_of_enemy_boats == 0:
                    connection.sendall(bytes("You lose!", "utf-8"))
                    connection.close()
                if 0 <= int(str(data.decode("utf-8"))[1]) < 5 and 0 <= int(str(data.decode("utf-8"))[2]) < 5:
                    first_position = int(str(data.decode("utf-8"))[1])
                    second_position = int(str(data.decode("utf-8"))[2])
                    if board_game[first_position][second_position] == 1:
                        enemy_hit = 1
                        board_game[first_position][second_position] = 0
                        print("We got hit!")
                    else:
                        print("Enemy missed!")
                    if our_boats_number == 0:
                        message_to_sent = "You win!"
                        print("We lose!")
                        connection.sendall(bytes(message_to_sent, "utf-8"))
                        connection.close()
                        stop_game = 0
                        break
                # Print our game board
                print("Our board: ")
                for i in range(5):
                    for j in range(5):
                        print((str(board_game[i][j]) + " "), end=" ")
                    print()
                # Get the position to attack the enemy boats
                row_to_hit = random.randrange(0, 5)
                column_to_hit = random.randrange(0, 5)
                print("Row to attack: " + str(row_to_hit))
                print("Column to attack: " + str(column_to_hit))
                message_to_sent = str(enemy_hit) + str(row_to_hit) + str(column_to_hit)
                connection.sendall(bytes(message_to_sent, 'utf-8'))
            elif data:
                # If received data is a message
                connection.sendall(bytes("The received data is ", 'utf-8') + data)
                if data.decode("utf-8") == "You lose!":
                    stop_game = 0
                    print("We lose!")
                    break
                if data.decode("utf-8") == "You win!":
                    stop_game = 0
                    print("We win!")
                    break
            else:
                # If no data were got than stop the game
                print('No more data from ' + str(client_address))
                break
            # Continue the game
            if stop_game == 1:
                data = connection.recv(1024)
                print('Received: ' + str(data.decode('utf-8')))
    finally:
        # Clean up the connection
        connection.close()
        print("Connection closed!")
