from SlowPrint import slow_print

class Player:
    values = {
        "A": 11, "K": 10, "Q": 10, "J": 10,
        "10": 10, "9": 9, "8": 8, "7": 7,
        "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
    }

    p_score, d_score = 0, 0

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def draw_card(self, deck):
        self.hand.append(deck.draw())

    def calculation(self):
        total, aces = 0, 0
        for card in self.hand:
            value = card[:-1]
            total += Player.values[value]
            if value == "A":
                aces += 1
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def show_hand(self, hide_first = False):
        if hide_first:
            slow_print("?", *self.hand[1:])
        else:
            slow_print(*self.hand)

    def hand_reset(self):
        self.hand.clear()

if __name__ == "__main__":
    pass
