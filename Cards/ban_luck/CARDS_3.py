import random
import itertools

# generates the deck and card values
SUIT = 'scdh'
RANK = '23456789TJQKA'
DECK = tuple(''.join(card) for card in itertools.product(RANK, SUIT))
VAL = []
for a in range(9):
    VAL += [a+2] * 4
for _ in range(3):
    VAL += [10] * 4
VAL += [1] * 4
DECKVAL = dict(zip(DECK, VAL))
counter = 0


def shuffle():
    # shuffles the deck into random order
    global s_deck
    s_deck = random.sample(DECK, 52)


class Hand:

    global counter, s_deck

    def __init__(self):
        # deals 2 cards
        # sets up variables hand_sum and init_sum for totaling
        global counter
        self.cards = list(s_deck[counter:counter + 2])
        counter += 2
        self.hand_sum = 0
        self.init_sum = 0

    def sum_hand(self):
        # totals the hand
        self.hand_sum = 0
        self.init_sum = 0
        for b in range(len(self.cards)):
            self.init_sum += DECKVAL[self.cards[b]]
        if ('As' in self.cards or 'Ac' in self.cards or 'Ad' in self.cards or 'Ah' in self.cards)\
                and self.cards and self.init_sum + 10 <= 21:    # special ace rule conditions
            self.hand_sum = self.init_sum + 10
        else:
            self.hand_sum = self.init_sum

    def draw(self):
        # draws a card from the deck
        global counter
        self.cards += list(s_deck[counter:counter + 1])
        counter += 1

    def hit_or_stay(self, dealer):
        # asks the player if they want to hit or stay
        self.bust(dealer)
        print("\n\nDealer's Hand:", dealer.cards[0], "--")
        print("Your hand is:", self.cards, "   Your sum is:", self.hand_sum, "\n")
        choice = input("Hit or Stay? ").lower()
        if choice == 'hit':
            self.draw()
            self.hit_or_stay(dealer)
        elif choice == 'stay':
            self.total(dealer)
        else:
            print("Please enter hit or stay")
            self.hit_or_stay(dealer)

    def total(self, dealer):
        # determines winner
        if self.hand_sum > dealer.hand_sum:
            print("You won the hand")
        elif self.hand_sum < dealer.hand_sum:
            if dealer.hand_sum <= 21:
                print("You lost the hand")
            else:
                print("Dealer busted")
        else:
            print("You tied")
        print("Dealer's hand:", dealer.cards, "   Dealer's sum:", dealer.hand_sum)
        print("Your hand:", self.cards, "Your sum:", self.hand_sum)
        print("\n*******************\n")

    def bust(self, dealer):
        # checks for player busting
        self.sum_hand()
        if self.hand_sum > 21:
            print("YOU BUSTED\n")
            self.hand_sum = 0
            self.total(dealer)
        else:
            pass


class Dealer(Hand):

    def __init__(self):
        Hand.__init__(self)
        self.logic()

    def logic(self):
        # makes sure the dealer hits "soft 17"
        self.sum_hand()
        while self.hand_sum < 17:
            self.draw()
            self.sum_hand()


class Game:

    def __init__(self):
        # starts the game
        x = input("Would you like to play?").lower()
        if x == "yes":
            shuffle()
            player = Hand()
            dealer = Dealer()
            player.hit_or_stay(dealer)
        else:
            pass

if __name__ == '__main__':
    game = Game()
