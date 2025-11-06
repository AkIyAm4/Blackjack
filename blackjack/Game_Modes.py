from SlowPrint import slow_print
from Deck_Generator import Deck
from Mechanics import Player
import time
import sys

class Game:
    class OnePlayer:
        def __init__(self):
            self.deck = Deck()
            self.player = Player("You")
            self.dealer = Player("Dealer")

        def battle(self, announce, p, d, winner=None):
            slow_print("\nYour hand:")
            slow_print(*p[0:], f"Total: {self.player.calculation()}")
            slow_print("\nDealer's hand:")
            slow_print(*d[0:], f"Total: {self.dealer.calculation()}")
            slow_print(announce)
            if winner == "player":
                self.player.score += 1
            elif winner == "dealer":
                self.dealer.score += 1
            self.cont()

        def cont(self):
            slow_print(f"\nScore: You - {self.player.score}| Dealer - {self.dealer.score}")
            self.deck.deck_regen()
            while True:
                ask = input("\nDo you want to play another game? (y/n) ").lower()
                if ask == "y":
                    self.play_round()
                elif ask == "n":
                    slow_print(f"\nFinal Score: You - {self.player.score} | Dealer - {self.dealer.score}")
                    if self.player.score > self.dealer.score:
                        slow_print("\n===== You won! =====")
                    elif self.player.score == self.dealer.score:
                        slow_print("\n===== It's a tie! =====")
                    elif self.player.score < self.dealer.score:
                        slow_print("\n===== You lost! =====")
                    sys.exit()

        def play_round(self):
            self.player.hand_reset()
            self.dealer.hand_reset()

            for _ in range(2):
                self.player.draw_card(self.deck)
                self.dealer.draw_card(self.deck)

            slow_print(f"\nYour hand:")
            self.player.show_hand()
            slow_print(f"Total: {self.player.calculation()}")
            if self.player.calculation() == 21:
                slow_print("\nYou got a blackjack! You win.")
                self.player.score += 1
                self.cont()

            slow_print(f"\nDealer's hand:")
            self.dealer.show_hand(hide_first=True)
            if self.dealer.calculation() == 21:
                slow_print("\nDealer's Hand:")
                self.dealer.show_hand()
                slow_print(f"Total: {self.dealer.calculation()}")
                slow_print("\nThe dealer got a blackjack! the dealer wins.")
                self.dealer.score += 1
                self.cont()

            p_stand = False
            d_stand = False

            while not (p_stand and d_stand):
                if not p_stand:
                    choice = input("\nHit or Stand? ").lower()
                    if choice == "hit":
                        self.player.draw_card(self.deck)
                        slow_print("\nYou drew a card.")
                        time.sleep(0.5)
                        slow_print("\nYour hand:")
                        self.player.show_hand()
                        slow_print(f"Total: {self.player.calculation()}")
                        time.sleep(0.5)
                        if self.player.calculation() > 21:
                            slow_print("\nYou busted! The dealer wins.")
                            self.dealer.score += 1
                            self.cont()
                    elif choice == "stand":
                        p_stand = True
                    else:
                        slow_print("Invalid input, try again.")
                        continue

                if not d_stand:
                    if self.dealer.calculation() < 17:
                        self.dealer.draw_card(self.deck)
                        slow_print("\nThe dealer chose to hit and drew a card.")
                        time.sleep(0.5)
                        slow_print(f"\nDealer's hand:")
                        self.dealer.show_hand(hide_first=True)
                        time.sleep(0.5)
                        if self.dealer.calculation() > 21:
                            slow_print()
                            self.dealer.show_hand()
                            slow_print(f"Total: {self.dealer.calculation()}")
                            slow_print("\nThe dealer busted! You win.")
                            self.player.score += 1
                            self.cont()
                    else:
                        slow_print("\nThe dealer chose to stand.")
                        d_stand = True

            if p_stand and d_stand:
                slow_print("\n===== The battle begins! =====")
                if self.player.calculation() > self.dealer.calculation():
                    self.battle("\nYou won!", self.player.hand, self.dealer.hand, "player")

                elif self.player.calculation() < self.dealer.calculation():
                    self.battle("\nThe dealer won!", self.player.hand, self.dealer.hand, "dealer")

                elif self.player.calculation() == self.dealer.calculation():
                    self.battle("\nIt's a tie!", self.player.hand, self.dealer.hand)

    class TwoPlayers:
        def __init__(self):
            slow_print("\nUnder Maintenance.")

if __name__ == "__main__":
    while True:
        gm = input("Choose: 1. OnePlayer or 2. TwoPlayers - ")
        if gm == "1":
            game = Game.OnePlayer()
            game.play_round()
            break
        elif gm == "2":
            game = Game.TwoPlayers()
            break
        else:
            print("Invalid")
#
