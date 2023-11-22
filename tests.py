import unittest
from game import Game
from player import Player
from board import Board

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = Game(single_player_mode=False)
        self.board = self.game.board

    def test_initial_empty_board(self):
        for row in self.board.board:
            self.assertTrue(all(cell is None for cell in row))

    def test_initial_player_setup(self):
        self.assertEqual(len(self.game.players), 2)
        self.assertIn(self.game.players[0].symbol, ['X', 'O'])
        self.assertIn(self.game.players[1].symbol, ['X', 'O'])
        self.assertNotEqual(self.game.players[0].symbol, self.game.players[1].symbol)

    def test_draw_condition(self):
        self.board.board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
        self.assertIsNone(self.board.get_winner())
        self.assertTrue(self.board.is_full())

    def test_valid_move(self):
        self.assertTrue(self.board.make_move(0, 0, 'X'))

    def test_invalid_move(self):
        self.board.board[0][0] = 'X'
        self.assertFalse(self.board.make_move(0, 0, 'O'))

    def test_game_winner_detection(self):
        self.game.board.board = [['X', 'X', 'X'], [None, None, None], [None, None, None]]
        self.game.end_game()
        winner = self.game.board.get_winner()
        self.assertEqual(winner, 'X')

if __name__ == '__main__':
    unittest.main()

