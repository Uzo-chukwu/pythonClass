from game import Game

print("Welcome to My Tic-Tac-Toe Game 🎮\nMy Game, My Rules!")
print("Press 1 to agree and play, or any other key to exit.")

choice = input("> ")
if choice == '1':
    game = Game()
    game.play()
else:
    print("Goodbye!")

