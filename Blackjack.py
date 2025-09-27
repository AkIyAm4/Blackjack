import random
import sys
import time
import builtins

def slow_print(*args, sep=" ", end="\n", delay=0.025, flush=True):
    text = sep.join(map(str, args)) + end
    for char in text:
        builtins.print(char, end="", flush=flush)
        time.sleep(delay)

print = slow_print

deck = [r + s for s in ["♠", "♥", "♦", "♣"] for r in ["A", "K", "Q", "J"] + [str(n) for n in range(10, 1, -1)]]
random.shuffle(deck)
values = {
        "A": 11, "K": 10, "Q": 10, "J": 10,
        "10": 10, "9": 9, "8": 8, "7": 7,
        "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}

p_score = 0
d_score = 0

def deck_regen():
    return [r + s for s in ["♠", "♥", "♦", "♣"] for r in ["A", "K", "Q", "J"] + [str(n) for n in range(10, 1, -1)]]

def calculation(n_deck):
    total = 0
    aces = 0
    for card in n_deck:
        mod = card[:-1]
        if mod in values:
            total += values[mod]
            if mod == "A":
                aces += 1
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def cont():
    global deck

    if len(deck) < 6:
        print("\nRegenerating the deck, please wait...")
        time.sleep(3)
        deck = deck_regen()
        random.shuffle(deck)
        print("\nRegeneration done")

    while True:
        ask = input("\nDo you want to play another game? (y/n) ").lower()
        if ask == "y":
            game()
        elif ask == "n":
            print(f"\nScore: You - {p_score}| Dealer - {d_score}")
            sys.exit()

def battle(announce, p, d, winner = None):
    global p_score, d_score

    print("\nYour hand:")
    print(*p[0:], f"Total: {calculation(p)}")
    print("\nDealer's hand:")
    print(*d[0:], f"Total: {calculation(d)}")
    print(announce)
    if winner == "player":
        p_score += 1
    elif winner == "dealer":
        d_score += 1
    cont()

def game():
    global p_score, d_score
    player_hand = []
    dealer_hand = []

    for i in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

    print(f"\nYour hand:")
    print(*player_hand[0:])
    print(f"Total: {calculation(player_hand)}")
    if calculation(player_hand) == 21:
        print("\nYou got a blackjack! You win.")
        p_score += 1
        cont()
    print(f"\nDealer's hand:")
    print("?", *dealer_hand[1:])
    if calculation(dealer_hand) == 21:
        print("\nDealer's Hand:")
        print(*dealer_hand[0:])
        print("The dealer got a blackjack! the dealer wins.")
        d_score += 1
        cont()

    p_stand = False
    d_stand = False

    while not (p_stand and d_stand):
        if not p_stand:
            choice = input("\nHit or Stand? ").lower()
            if choice == "hit":
                player_hand.append(deck.pop())
                print("\nYou drew a card.")
                print("\nYour hand:")
                print(*player_hand[0:])
                print(f"Total: {calculation(player_hand)}")
                if calculation(player_hand) > 21:
                    print("\nYou busted! The dealer wins.")
                    d_score += 1
                    cont()
            elif choice == "stand":
                p_stand = True
            else:
                print("Invalid input, try again.")
                continue

        if not d_stand:
            if calculation(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
                print("\nThe dealer chose to hit and drew a card.")
                print(f"\nDealer's hand:")
                print("?", *dealer_hand[1:])
                if calculation(dealer_hand) > 21:
                    print()
                    print(*dealer_hand[0:])
                    print("The dealer busted! You win.")
                    p_score += 1
                    cont()
            else:
                print("\nThe dealer chose to stand.")
                d_stand = True

    if p_stand and d_stand:
        print("\n===== The battle begins! =====")
        if calculation(player_hand) > calculation(dealer_hand):
            battle("\nYou won!", player_hand, dealer_hand, "player")

        elif calculation(player_hand) < calculation(dealer_hand):
            battle("\nThe dealer won!", player_hand, dealer_hand, "dealer")

        elif calculation(player_hand) == calculation(dealer_hand):
            battle("\nIt's a tie!", player_hand, dealer_hand)

game()
