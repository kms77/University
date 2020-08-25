from unittest import TestCase
from Service.Service import Service
from Repository.Repository import Repo
from Exception.Exception import RepoError


class TestService(TestCase):
    def setUp(self):
        self.repo = Repo()
        self.service = Service(self.repo)
        self.board = self.service.create_board(6, 7)

    def test_create_board(self):
        self.assertEqual(self.board[0][0], 0)
        self.assertEqual(self.board[0][1], 0)
        self.assertEqual(self.board[0][2], 0)
        self.assertEqual(self.board[0][3], 0)
        self.assertEqual(self.board[0][4], 0)
        self.assertEqual(self.board[0][5], 0)
        self.assertEqual(self.board[0][6], 0)
        self.assertEqual(self.board[1][0], 0)
        self.assertEqual(self.board[1][1], 0)
        self.assertEqual(self.board[1][2], 0)
        self.assertEqual(self.board[1][3], 0)
        self.assertEqual(self.board[1][4], 0)
        self.assertEqual(self.board[1][5], 0)
        self.assertEqual(self.board[1][6], 0)
        self.assertEqual(self.board[2][0], 0)
        self.assertEqual(self.board[2][1], 0)
        self.assertEqual(self.board[2][2], 0)
        self.assertEqual(self.board[2][3], 0)
        self.assertEqual(self.board[2][4], 0)
        self.assertEqual(self.board[2][5], 0)
        self.assertEqual(self.board[2][6], 0)
        self.assertEqual(self.board[3][0], 0)
        self.assertEqual(self.board[3][1], 0)
        self.assertEqual(self.board[3][2], 0)
        self.assertEqual(self.board[3][3], 0)
        self.assertEqual(self.board[3][4], 0)
        self.assertEqual(self.board[3][5], 0)
        self.assertEqual(self.board[3][6], 0)
        self.assertEqual(self.board[4][0], 0)
        self.assertEqual(self.board[4][1], 0)
        self.assertEqual(self.board[4][2], 0)
        self.assertEqual(self.board[4][3], 0)
        self.assertEqual(self.board[4][4], 0)
        self.assertEqual(self.board[4][5], 0)
        self.assertEqual(self.board[4][6], 0)
        self.assertEqual(self.board[5][0], 0)
        self.assertEqual(self.board[5][1], 0)
        self.assertEqual(self.board[5][2], 0)
        self.assertEqual(self.board[5][3], 0)
        self.assertEqual(self.board[5][4], 0)
        self.assertEqual(self.board[5][5], 0)
        self.assertEqual(self.board[5][6], 0)

    def test_full_table(self):
        self.board = self.service.create_board(6, 7)
        i = self.repo.full_table(self.board, 6, 7)
        self.assertEqual(i, False)
        self.board[0][0] = 1
        self.board[0][1] = 2
        self.board[0][2] = 1
        self.board[0][3] = 2
        self.board[0][4] = 1
        self.board[0][5] = 2
        self.board[0][6] = 1
        self.board[1][0] = 1
        self.board[1][1] = 2
        self.board[1][2] = 1
        self.board[1][3] = 2
        self.board[1][4] = 1
        self.board[1][5] = 2
        self.board[1][6] = 1
        self.board[2][0] = 2
        self.board[2][1] = 1
        self.board[2][2] = 2
        self.board[2][3] = 1
        self.board[2][4] = 2
        self.board[2][5] = 1
        self.board[2][6] = 2
        self.board[3][0] = 2
        self.board[3][1] = 1
        self.board[3][2] = 2
        self.board[3][3] = 1
        self.board[3][4] = 2
        self.board[3][5] = 1
        self.board[3][6] = 2
        self.board[4][0] = 1
        self.board[4][1] = 2
        self.board[4][2] = 1
        self.board[4][3] = 2
        self.board[4][4] = 1
        self.board[4][5] = 2
        self.board[4][6] = 1
        self.board[5][0] = 2
        self.board[5][1] = 2
        self.board[5][2] = 2
        self.board[5][3] = 1
        self.board[5][4] = 1
        self.board[5][5] = 1
        self.board[5][6] = 1
        i = self.service.full_table(self.board, 6, 7)
        self.assertEqual(i, True)

    def test_row(self):
        self.board = self.service.create_board(6, 7)
        i = self.service.row(self.board, 6, 1)
        self.assertEqual(i, 0)
        self.board[0][1] = 1
        self.board[1][1] = 1
        self.board[2][1] = 2
        i = self.service.row(self.board, 6, 1)
        self.assertEqual(i, 3)
        self.board[3][1] = 1
        self.board[4][1] = 2
        self.board[5][1] = 2
        self.assertRaises(RepoError, self.service.row, self.board, 6, 1)

    def test_update(self):
        self.board = self.service.move(self.board, 0, 2, 1)
        self.assertEqual(self.board[0][2], 1)
        i = self.service.row(self.board, 6, 2)
        self.assertEqual(i, 1)

    def test_win_game(self):
        self.board = self.service.create_board(6, 7)
        result = self.service.win(self.board, 1, 2, 6, 7)
        self.assertEqual(result, False)
        self.board[1][1] = 1
        self.board[1][2] = 1
        self.board[1][3] = 1
        self.board[1][4] = 1
        result = self.service.win(self.board, 1, 4, 6, 7)
        self.assertEqual(result, True)
        self.board = self.service.create_board(6, 7)
        result = self.service.win(self.board, 3, 4, 6, 7)
        self.assertEqual(result, False)
        self.board[2][6] = 2
        self.board[3][6] = 2
        self.board[4][6] = 2
        self.board[5][6] = 2
        result = self.service.win(self.board, 5, 6, 6, 7)
        self.assertEqual(result, True)
        self.board = self.service.create_board(6, 7)
        result = self.service.win(self.board, 2, 4, 6, 7)
        self.assertEqual(result, False)
        self.board[0][1] = 1
        self.board[0][2] = 2
        self.board[1][2] = 1
        self.board[0][3] = 2
        self.board[1][3] = 1
        self.board[0][4] = 2
        self.board[2][3] = 1
        self.board[1][4] = 1
        self.board[2][4] = 2
        self.board[3][4] = 1
        result = self.service.win(self.board, 3, 4, 6, 7)
        self.assertEqual(result, True)

    def test_block(self):
        self.board = self.service.create_board(6, 7)
        x = -1
        x = self.service.block(self.board, 6, 7, x)
        self.assertEqual(x, -1)
        x = -1
        self.board[0][0] = 1
        self.board[0][1] = 2
        self.board[0][2] = 1
        self.board[0][3] = 2
        self.board[0][4] = 1
        self.board[0][5] = 2
        self.board[0][6] = 1
        self.board[1][0] = 1
        self.board[1][1] = 1
        self.board[1][2] = 1
        self.board[1][3] = 1
        self.board[1][4] = 0
        x = self.service.block(self.board, 6, 7, x)
        self.assertEqual(x, 4)
        self.board = self.service.create_board(6, 7)
        x = -1
        self.board[2][6] = 1
        self.board[3][6] = 1
        self.board[4][6] = 1
        self.board[5][6] = 0
        x = self.service.block(self.board, 6, 7, x)
        self.assertEqual(x, 6)
        self.board = self.service.create_board(6, 7)
        x = -1
        self.board[0][0] = 1
        self.board[1][1] = 2
        self.board[0][1] = 1
        self.board[0][2] = 2
        self.board[1][2] = 1
        self.board[0][3] = 2
        self.board[1][3] = 1
        self.board[0][4] = 2
        self.board[2][3] = 1
        self.board[1][4] = 1
        self.board[2][4] = 2
        self.board[3][4] = 0
        x = self.service.block(self.board, 6, 7, x)
        self.assertEqual(x, 4)
