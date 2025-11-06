import random
import time
from SlowPrint import slow_print

def shuffling_choice():
    slow_print("===== Shuffling Methods =====")
    slow_print("1. Random Shuffle")
    slow_print("2. Riffle Shuffle")
    while True:
        try:
            choice = int(input("Choose a shuffling method: "))

            deck = Shuffling()

            if choice == 1:
                deck.random()
                return deck.cards

            elif choice == 2:
                slow_print("Under Maintenance.")

            else:
                slow_print("Input is out of option's range, try again.")

        except ValueError:
            slow_print("Invalid input, try again.")

class Shuffling:
    def __init__(self):
        self.cards = [r + s for s in ["♠", "♥", "♦", "♣"]
                      for r in ["A", "K", "Q", "J"] + [str(n) for n in range(10, 1, -1)]]

    def random(self):
        random.shuffle(self.cards)
        return self.cards

    def riffle(self):
        
        pass

class Deck:
    def __init__(self):
        self.cards = shuffling_choice()

    def draw(self):
        return self.cards.pop()

    def deck_regen(self):
        if len(self.cards) < 11:
            slow_print("\nRegenerating the deck, please wait...")
            time.sleep(2)
            self.__init__()
            slow_print("\nRegeneration done.")

if __name__ == "__main__":
    cards = Deck().cards
    count = 0
    for card in cards:
        slow_print(card, end=" ")
        count += 1
        if count % 13 == 0:
            print()
