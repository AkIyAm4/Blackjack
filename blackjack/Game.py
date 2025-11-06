from SlowPrint import slow_print
from GameModes import Game

def main():
    slow_print("===== Welcome to Blackjack =====\n")
    slow_print("===== Game Modes =====")
    slow_print("1. You vs AI")
    slow_print("2. You vs Another Human")
    while True:
        try:
            gm_choice = int(input("\nChoose a game mode: "))
            if gm_choice == 1:
                game = Game.OnePlayer()
                game.play_round()
                break

            elif gm_choice == 2:
                game = Game.TwoPlayers()

            else:
                slow_print("Out of option's range, try again.")

        except ValueError:
            slow_print("Invalid input, try again.")

if __name__ == "__main__":
    main()
