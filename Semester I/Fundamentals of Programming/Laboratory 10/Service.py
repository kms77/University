class Service:
    def __init__(self, repo):
        self.__repo = repo

    def full_table(self, board, table_row, table_column):
        '''
        param board: connect 4-game table 6x7 size
        param table_row: the parameter which has the value 6(rows has the table)
        param table_column: the parameter which has the value 7(columns has the table)
        return: True-all the table is occupied by pieces, False- at least one place is not occupied
        '''
        return self.__repo.full_table(board, table_row, table_column)

    def create_board(self, row, column):
        '''

        param row: how much rows the table will have
        param column: how much columns the table will have
        return: the board with zero values and size: row X column
        '''
        return self.__repo.create_board(row, column)

    def row(self, board, table_row, column):
        '''

        param board: the board with 6x7 size
        param table_row: the numbers of rows-6
        param column: the current column
        return: the place with the smallest zero value
        '''
        return self.__repo.search(board, table_row, column)

    def move(self, board, x, y, player):
        '''
        param board: the board with 6x7 size
        param x: the value of the row
        param y: the value of the column
        param player: the player which had the move
        return: the board changed by the value of the move
        '''
        return self.__repo.update(board, x, y, player)

    def win(self, board, x, y, table_row, table_column):
        '''
        param board: the board with 6x7 size
        param x: the value of the current row
        param y: the value of the current column
        param table_row: the numbers of rows(6)
        param table_column: the number of columns(7)
        return: True: the game is over because someone won, False: the game can continue
        '''
        g = False
        g = self.__repo.horizontal(board, x, table_column)
        if g == False:
            g = self.__repo.vertical(board, y, table_row)
        if g == False:
            g = self.__repo.diagonal(board, table_row, table_column)
        return g

    def block(self, board, table_row, table_column, x):
        '''
        param board: the board with 6x7 size
        param table_row: the number of rows(6)
        param table_column: the number of columns(7)
        param x: the param with an -1 initial value/it's value will be change only if the player can does a winning move
        return: x
        '''
        return self.__repo.block(board, table_row, table_column, x)
