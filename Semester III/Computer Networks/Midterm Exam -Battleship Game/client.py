import socket

# Create a TCP/IP socket
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 2764)
print('Connecting to ' + str(server_address))
Socket.connect(server_address)
try:
    # Hard coded values
    board_game = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
    amount_received = 0
    our_boats_number = 3
    number_of_enemy_boats = 3
    amount_expected = 2048
    initial_attack = 0
    # The data flow model is based on 3 chars:
    # first is the previous hit result
    # second one is the row we are going to attack
    # third is the collum we are going to attack
    while True:
        enemy_hit = 0
        if initial_attack == 0:
            # first move is the client move
            # the initial move message will have the value zero for the hit result
            # the message will return input values just for the row and the column to attack
            row_to_hit = input("Row to attack: ")
            column_to_hit = input("Column to attack: ")
            initial_attack = 1
            message_to_sent = bytes("0" + str(row_to_hit) + str(column_to_hit), 'utf-8')
            Socket.sendall(message_to_sent)
        else:
            data = Socket.recv(amount_expected)
            print('Received: ' + str(data.decode('utf-8')))
            amount_received += len(data)
            # We verify the received data: if we hit or not an enemy boat and if we got hit
            if str(data.decode("utf-8"))[0] == "1":
                number_of_enemy_boats = number_of_enemy_boats - 1
                print("We hit enemy!")
                if number_of_enemy_boats == 0:
                    print("We win!")
                    Socket.sendall(bytes("You lose!", "utf-8"))
                    Socket.close()
                    break

            else:
                print("We missed enemy!")
            if 0 <= int(str(data.decode("utf-8"))[1]) < 5 and 0 <= int(str(data.decode("utf-8"))[2]) < 5:
                first_position = int(str(data.decode("utf-8"))[1])
                second_position = int(str(data.decode("utf-8"))[2])
                if board_game[first_position][second_position] == 1:
                    enemy_hit = 1
                    print("We got hit!")
                    board_game[first_position][second_position] = 0
                    our_boats_number = our_boats_number - 1
                    if our_boats_number == 0:
                        print("We lose!")
                        Socket.sendall(bytes("You win!", "utf-8"))
                        Socket.close()
                        break
                else:
                    print("Enemy missed!")
            # Print our game board
            print("Our board: ")
            for i in range(5):
                for j in range(5):
                    print(str(board_game[i][j]) + " ", end=" ")
                print()
            # Get the position to attack the enemy boats
            row_to_hit = input("Row to attack: ")
            column_to_hit = input("Column to attack: ")
            message_to_sent = bytes(str(enemy_hit) + str(row_to_hit) + str(column_to_hit), 'utf-8')
            Socket.sendall(message_to_sent)
finally:
    Socket.close()
Socket.close()
