

class TicTacToe(object):
    __rolls = []

    def __init__(self):
        self.__rolls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        pass

    def run_game(self, *args):
        if args[0] == -1:
            applicant = raw_input("What is your name: ")
            print("Hello " + applicant + " lets play tic-tac-toe")

        for i in range(len(args)):
            location = self.getInput(args, i)

            if location.isdigit():
                location_int = int(location)
                if 0 < location_int < 10:
                    row_location = self.get_row_location(location_int)
                    column_location = self.get_column_location(location_int)
                    if i % 2 == 0:
                        self.__rolls[row_location][column_location] = 'x'
                    else:
                        self.__rolls[row_location][column_location] = 'o'


            print("Maybe later")
            self.print_ttt_board()

    def getInput(self, args, location):
        self.print_ttt_board()
        print("What position do you want to play?")
        if args[0] != -1:
            print("Choose a location: " + args[location])
            return args[location]
        else:
            location = raw_input("Choose a location: ")
            return location

    def get_column_location(self, param):
        return (param - 1) % 3

    def get_row_location(self, param):
        return (param - 1) / 3

    def print_ttt_board(self):
        self.get_printable_ttt_board()

    def get_printable_ttt_board(self):
        board_printout = ''
        for row in self.__rolls:
            for column in row:
                board_printout += str(column)
                board_printout += ' '
            board_printout += '\n'
        return board_printout


def main():
    ttt = TicTacToe()
    ttt.run_game(-1, -1, -1, -1, -1, -1, -1, -1, -1)


if __name__ == "__main__":
    main()

