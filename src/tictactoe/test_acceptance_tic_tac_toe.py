# -*- coding: utf-8 -*- #
import unittest

from src.tictactoe.tic_tac_toe import TicTacToe


class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        self.ttt = TicTacToe()

    def test_run_game_full_acceptance_test(self):
        self.ttt.run_game()
