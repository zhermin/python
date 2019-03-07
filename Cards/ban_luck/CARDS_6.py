import random

deck = {"Ace" : 11, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10}
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]


name, value = random.choice (list(deck.items()))
suit = random.choice(suit)



name_num = random.choice (list(deck.items()))
for num in range(6):
    print(name_num, sep="")
    
    print(name_1)

