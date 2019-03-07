import random



deck = {"Ace" : 11, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10}
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]

class RandomCard:
    
    def __init__(self, name, suit):

        self.name = name
        self.suit = suit

    def printCard(self, cardID):

        print (card1.name + " of " + card1.suit)

card1 = RandomCard(random.choice (list(deck.keys())), random.choice(suit))
card2 = RandomCard(random.choice (list(deck.keys())), random.choice(suit))
card3 = RandomCard(random.choice (list(deck.keys())), random.choice(suit))
card4 = RandomCard(random.choice (list(deck.keys())), random.choice(suit))
card5 = RandomCard(random.choice (list(deck.keys())), random.choice(suit))



card1.printCard(card1)
