from Exception.Exception import RepoError
import numpy as ny


class Repo:
    def __init__(self):
        pass

    @staticmethod
    def full_table(board, table_row, table_column):
        '''
        param board: a matrix board
        param table_row: the number of rows contained by the matrix
        param table_column: the number of columns contained by the matrix
        return: True: the matrix is full of pieces and no one move can be done / False: at least one move can be done
        '''
        g = True
        for i in range(table_row):
            for j in range(table_column):
                if board[i][j] == 0 and g == True:
                    g = False
        return g

    @staticmethod
    def create_board(row, column):
        '''
        param row: number of rows for the new board
        param column: number of columns foe the new board
        return: it returns a board with a row x column size, with zero values
        '''
        board = ny.zeros((row, column))
        return board

    @staticmethod
    def search(board, table_row, column):
        '''
        param board: a board with a row x column size
        param table_row: how much rows the board has
        param column: a column number from the board
        return: the free place from the column of the board
        '''
        g = 0
        for i in range(int(table_row)):
            if board[i][int(column)] == 0:
                g = 1
                return i
        if g == 0:
            raise RepoError("RepoError:impossible move!")

    @staticmethod
    def update(board, x, y, player):
        '''
        param board: a board with a row x column size
        param x: the x position from the board
        param y: the y position from the board
        param player: the new value for board[x][y] element from the board
        return: an updated board with the element board[x][y] changed
        '''
        board[x][y] = player
        return board

    @staticmethod
    def horizontal(board, x, table_column):
        '''
        param board: a board with a row x column size
        param x: the number of the row from the board
        param table_column: number of columns
        return: this function verifies if there is 4 elements with the same value on the x row from the board
        '''
        for i in range(table_column - 3):
            if board[x][i] == board[x][i + 1] == board[x][i + 2] == board[x][i + 3] != 0:
                return True
        return False

    @staticmethod
    def vertical(board, y, table_row):
        '''
        param board: a board with a row x column size
        param y: the number of the column from the board
        param table_row: number of rows
        return: this function verifies if there is 4 elements with the same value on the y column from the board
        '''
        for i in range(table_row - 3):
            if board[i][y] == board[i + 1][y] == board[i + 2][y] == board[i + 3][y] != 0:
                return True
        return False

    @staticmethod
    def diagonal(board, table_row, table_column):
        '''
        param board: a board with a row x column size
        param table_row: the number of rows
        param table_column: the number of columns
        return: this function verifies if there is 4 elements with the same value on a diagonal of the board
        '''
        for i in range(table_row - 3):
            for j in range(table_column - 3):
                if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] != 0:
                    return True
        for j in range(table_column - 3):
            for i in range(3, table_row):
                if board[i][j] == board[i - 1][j + 1] == board[i - 2][j + 2] == board[i - 3][j + 3] != 0:
                    return True
        return False

    def block(self, board, table_row, table_column, x):
        '''
        param board: a board with row x column size
        param table_row: the number of rows
        param table_column: the number of columns
        param x: the parameter with a -1 initial value
        return: x=-1 no one winning chance for the player, x= a new value if there is a chance for the player to win
                the game
        '''
        g = 0
        for i in range(table_row):
            for j in range(table_column):
                if board[i][j] == 0 and g == 0:
                    self.update(board, i, j, 1)
                    if self.horizontal(board, i, table_column) == True:
                        if board[i - 1][j] != 0 or i == 0:
                            x = j
                            g = 1
                    self.update(board, i, j, 0)
        if g == 0:
            for i in range(table_row):
                for j in range(table_column):
                    if board[i][j] == 0 and g == 0:
                        self.update(board, i, j, 1)
                        if self.vertical(board, j, table_row) == True:
                            if board[i - 1][j] != 0 or i == 0:
                                x = j
                                g = 1
                        self.update(board, i, j, 0)
        if g == 0:
            for i in range(table_row):
                for j in range(table_column):
                    if board[i][j] == 0 and g == 0:
                        self.update(board, i, j, 1)
                        if self.diagonal(board, table_row, table_column) == True:
                            if board[i - 1][j] != 0 or i == 0:
                                x = j
                                g = 1
                        self.update(board, i, j, 0)
        return x
