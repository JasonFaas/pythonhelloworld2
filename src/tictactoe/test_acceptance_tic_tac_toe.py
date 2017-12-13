# -*- coding: utf-8 -*- #
import unittest

from src.tictactoe.tic_tac_toe import TicTacToe


class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        self.ttt = TicTacToe()

    def test_run_game_full_acceptance_test_with_single_input(self):
        self.ttt.run_game('4')
        board = self.ttt.get_printable_ttt_board()
        self.assertEqual('1 2 3 \nx 5 6 \n7 8 9 \n', board, "what happened?" + board + "?")

    def test_run_game_full_acceptance_test_with_multiple_input(self):
        self.ttt.run_game('4', '5')
        board = self.ttt.get_printable_ttt_board()
        self.assertEqual('1 2 3 \nx o 6 \n7 8 9 \n', board, "what happened?" + board + "?")