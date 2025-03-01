import unittest
from board import Board
from player import PlayerX, PlayerO
from game import Game

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_board_empty(self):
        self.assertEqual(self.board.board, [' '] * 9)

    def test_place_symbol(self):
        self.board.place_symbol(0, 'X')
        self.assertEqual(self.board.board[0], 'X')

    def test_place_symbol_invalid(self):
        self.board.place_symbol(0, 'X')
        result = self.board.place_symbol(0, 'O')
        self.assertFalse(result)

    def test_is_winner_row(self):
        self.board.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(self.board.is_winner('X'))

    def test_is_winner_column(self):
        self.board.board = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
        self.assertTrue(self.board.is_winner('O'))

    def test_is_winner_diagonal(self):
        self.board.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(self.board.is_winner('X'))

    def test_is_draw(self):
        self.board.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertTrue(self.board.is_draw())

    def test_is_not_draw(self):
        self.board.board = ['X', 'O', ' ', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertFalse(self.board.is_draw())

    def test_is_empty(self):
        self.assertTrue(self.board.is_empty(0))
        self.board.place_symbol(0, 'X')
        self.assertFalse(self.board.is_empty(0))

    def test_reset(self):
        self.board.place_symbol(0, 'X')
        self.board.reset()
        self.assertEqual(self.board.board, [' '] * 9)


class TestPlayerX(unittest.TestCase):
    def setUp(self):
        self.player = PlayerX()
        self.board = Board()

    def test_player_symbol(self):
        self.assertEqual(self.player.symbol, 'X')


class TestPlayerO(unittest.TestCase):
    def setUp(self):
        self.player = PlayerO()
        self.board = Board()

    def test_player_symbol(self):
        self.assertEqual(self.player.symbol, 'O')


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_scores(self):
        self.assertEqual(self.game.scores, {'X': 0, 'O': 0, 'Draws': 0})

    def test_reset_game(self):
        self.game.scores['X'] = 1
        self.game.scores['O'] = 1
        self.game.scores['Draws'] = 1
        self.game.reset_game()
        self.assertEqual(self.game.scores, {'X': 0, 'O': 0, 'Draws': 0})


if __name__ == '__main__':
    unittest.main()
