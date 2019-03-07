import random



deck = {"Ace" : 11, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10}
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]

def play():
    
    name_1, value_1 = random.choice (list(deck.items()))
    name_2, value_2 = random.choice (list(deck.items()))
    name_3, value_3 = random.choice (list(deck.items()))
    name_4, value_4 = random.choice (list(deck.items()))
    name_5, value_5 = random.choice (list(deck.items()))

    suit_1 = random.choice(suit)
    suit_2 = random.choice(suit)
    suit_3 = random.choice(suit)
    suit_4 = random.choice(suit)
    suit_5 = random.choice(suit)

    card_1 = name_1 + " of " + suit_1
    card_2 = name_2 + " of " + suit_2
    card_3 = name_3 + " of " + suit_3
    card_4 = name_4 + " of " + suit_4
    card_5 = name_5 + " of " + suit_5


    hand = [card_1, card_2, card_3, card_4, card_5]
    total = [value_1, value_2]


    while True:
        if card_1 != card_2 != card_3 != card_4 != card_5:
            print(hand)
            break
        else:
            play()
            break
        
play()
