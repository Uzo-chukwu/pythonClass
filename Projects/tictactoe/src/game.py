from board import Board
from player import PlayerX, PlayerO

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.scores = {'X': 0, 'O': 0, 'Draws': 0}

    def setup_players(self):
        print("The first player is Player X.")
        print("The second player is Player O.")
        self.players.append(PlayerX())
        self.players.append(PlayerO())

    def play(self):
        self.setup_players()
        current_player_index = 0

        while True:
            self.board.display()
            current_player = self.players[current_player_index]
            move = current_player.get_move(self.board)
            self.board.place_symbol(move, current_player.symbol)

            if self.board.is_winner(current_player.symbol):
                self.board.display()
                print(f"Player {current_player.symbol} wins!")
                self.scores[current_player.symbol] += 1
                break

            if self.board.is_draw():
                self.board.display()
                print("It's a draw!")
                self.scores['Draws'] += 1
                break

            current_player_index = 1 - current_player_index

        self.display_scores()

        if self.play_again():
            self.reset_game()
            self.play()
        else:
            print("Thanks for playing!")

    def display_scores(self):
        print("\nScores:")
        print(f"Player X: {self.scores['X']}")
        print(f"Player O: {self.scores['O']}")
        print(f"Draws: {self.scores['Draws']}\n")

    def play_again(self):
        return input("Play again? (y/n): ").strip().lower() == 'y'

    def reset_game(self):
        self.board.reset()
