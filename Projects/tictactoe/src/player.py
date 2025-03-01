class PlayerX:
    def __init__(self):
        self.symbol = "X"

    def get_move(self, board):
        while True:
            try:
                move = int(input(f"Player {self.symbol}, enter your move (1-9): ")) - 1
                if move in range(9) and board.is_empty(move):
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")


class PlayerO(PlayerX):
    def __init__(self):
        self.symbol = "O"

