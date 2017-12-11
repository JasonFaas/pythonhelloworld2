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
            locationInt = int(location)
            if locationInt > 0 and locationInt < 10:
                print 'awesome'
                rowLocation = (locationInt % 3)
                columnLocation = locationInt / 3
                print rowLocation, columnLocation
                self.rolls[rowLocation][columnLocation] = 'x'
        else:
            print 'terrible'

        print("Maybe later")
        self.print_columns()

    def get_column_location(self, param):
        return (param % 3) - 1

    def get_row_location(self, param):
        return param / 3

    def print_columns(self):
        for row in self.rolls:
            for column in row:
                print column,
            print ''
