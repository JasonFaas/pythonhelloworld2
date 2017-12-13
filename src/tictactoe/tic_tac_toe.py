
import sys


class TicTacToe(object):

    def __init__(self):
        self.rolls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


    def run_game(self):
        # applicant = raw_input("What is your name: ") TODO Turn this back on
        applicant = 'Jason'
        print("Hello " + applicant + " lets play tic-tac-toe")
        print("What position do you want to play first?")

        self.print_columns()

        location = raw_input("Choose a location: ")
        if location.isdigit():
            location_int = int(location)
            if 0 < location_int < 10:
                row_location = (location_int % 3)
                column_location = location_int / 3
                print row_location, column_location
                self.rolls[row_location][column_location] = 'x'

        print("Maybe later")
        self.print_columns()

    def get_column_location(self, param):
        return (param - 1) % 3

    def get_row_location(self, param):
        return (param - 1) / 3

    def print_columns(self):
        for row in self.rolls:
            for column in row:
                print column,
            print ''


def main():
    TicTacToe().run_game()


if __name__ == "__main__":
    main()

