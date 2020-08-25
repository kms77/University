from unittest import TestCase
from Repository.Repository import Repo
from Exception.Exception import RepoError


class TestRepo(TestCase):
    def setUp(self):
        self.repo = Repo()
        self.board = self.repo.create_board(6, 7)

    def test_full_table(self):
        self.board = self.repo.create_board(6, 7)
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
        i = self.repo.full_table(self.board, 6, 7)
        self.assertEqual(i, True)

    def test_board(self):
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

    def test_search(self):
        i = self.repo.search(self.board, 6, 1)
        self.assertEqual(i, 0)
        self.board[0][1] = 1
        self.board[1][1] = 1
        self.board[2][1] = 2
        i = self.repo.search(self.board, 6, 1)
        self.assertEqual(i, 3)
        self.board[3][1] = 1
        self.board[4][1] = 2
        self.board[5][1] = 2
        self.assertRaises(RepoError, self.repo.search, self.board, 6, 1)

    def test_update(self):
        self.board = self.repo.update(self.board, 0, 2, 1)
        self.assertEqual(self.board[0][2], 1)
        i = self.repo.search(self.board, 6, 2)
        self.assertEqual(i, 1)

    def test_horizontal(self):
        self.board = self.repo.create_board(6, 7)
        result = self.repo.horizontal(self.board, 1, 7)
        self.assertEqual(result, False)
        self.board[1][1] = 1
        self.board[1][2] = 1
        self.board[1][3] = 1
        self.board[1][4] = 1
        result = self.repo.horizontal(self.board, 1, 7)
        self.assertEqual(result, True)

    def test_vertical(self):
        self.board = self.repo.create_board(6, 7)
        result = self.repo.vertical(self.board, 6, 6)
        self.assertEqual(result, False)
        self.board[2][6] = 2
        self.board[3][6] = 2
        self.board[4][6] = 2
        self.board[5][6] = 2
        result = self.repo.vertical(self.board, 6, 6)
        self.assertEqual(result, True)

    def test_diagonal(self):
        self.board = self.repo.create_board(6, 7)
        result = self.repo.diagonal(self.board, 6, 7)
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
        result = self.repo.diagonal(self.board, 6, 7)
        self.assertEqual(result, True)

    def test_block(self):
        self.board = self.repo.create_board(6, 7)
        x = -1
        x = self.repo.block(self.board, 6, 7, x)
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
        x = self.repo.block(self.board, 6, 7, x)
        self.assertEqual(x, 4)
        self.board = self.repo.create_board(6, 7)
        x = -1
        self.board[2][6] = 1
        self.board[3][6] = 1
        self.board[4][6] = 1
        self.board[5][6] = 0
        x = self.repo.block(self.board, 6, 7, x)
        self.assertEqual(x, 6)
        self.board = self.repo.create_board(6, 7)
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
        x = self.repo.block(self.board, 6, 7, x)
        self.assertEqual(x, 4)
