class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def display(self):
        print("\n")
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print("\n")

    def is_winner(self, symbol):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == symbol:
                return True
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] == symbol:
                return True
        if self.board[0] == self.board[4] == self.board[8] == symbol:
            return True
        if self.board[2] == self.board[4] == self.board[6] == symbol:
            return True
        return False

    def is_draw(self):
        return ' ' not in self.board and not self.is_winner('X') and not self.is_winner('O')

    def is_empty(self, position):
        return self.board[position] == ' '

    def place_symbol(self, position, symbol):
        if 0 <= position < 9 and self.is_empty(position):
            self.board[position] = symbol
            return True
        return False

    def reset(self):
        self.board = [' ' for _ in range(9)]
