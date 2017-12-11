# -*- coding: utf-8 -*- #
import unittest

from src.tictactoe.tic_tac_toe import TicTacToe


class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        self.ttt = TicTacToe()

    def test_run_game_full_acceptance_test(self):
        self.ttt.run_game()

    def test_location_input_to_double_array_user_1(self):
        user_location = 1
        column_location = self.ttt.get_column_location(user_location)
        row_location = self.ttt.get_row_location(user_location)
        self.assertEqual(0, column_location)
        self.assertEqual(0, row_location)

    def test_location_input_to_double_array_user_2(self):
        user_location = 2
        column_location = self.ttt.get_column_location(user_location)
        row_location = self.ttt.get_row_location(user_location)
        self.assertEqual(1, column_location)
        self.assertEqual(0, row_location)

    def test_location_input_to_double_array_user_4(self):
        user_location = 4
        column_location = self.ttt.get_column_location(user_location)
        row_location = self.ttt.get_row_location(user_location)
        self.assertEqual(0, column_location)
        self.assertEqual(1, row_location)

