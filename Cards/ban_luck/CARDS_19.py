import random, pprint

deck = {"Ace" : 11, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10}
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]

class Money:

    def __init__(self):
        self.cash = 100
        self.round = 1
        
    def win(self, k_win):
        self.cash += self.bet * k_win

    def lose(self, k_lose):
        self.cash -= self.bet * k_lose

    def checkCash(self):
        
        print ("=".center(77, "="))
        print (("[Cash = $" + str(self.cash) + "]").center(77, "-"))
        print ("=".center(77, "="))

    def endRound(self):
        self.round += 1

    def checkRound(self):
        print (("[Round " + str(self.round) + "]").center(77, "*"))

dough = Money()



while True:

        # Player Card Generator
        name_1, value_1 = random.choice (list(deck.items()))
        name_2, value_2 = random.choice (list(deck.items()))
        name_3, value_3 = random.choice (list(deck.items()))
        name_4, value_4 = random.choice (list(deck.items()))
        name_5, value_5 = random.choice (list(deck.items()))

        # CPU Card Generator
        name_6, value_6 = random.choice (list(deck.items()))
        name_7, value_7 = random.choice (list(deck.items()))
        name_8, value_8 = random.choice (list(deck.items()))
        name_9, value_9 = random.choice (list(deck.items()))
        name_10, value_10 = random.choice (list(deck.items()))


        # Player Suits
        suit_1 = random.choice(suit)
        suit_2 = random.choice(suit)
        suit_3 = random.choice(suit)
        suit_4 = random.choice(suit)
        suit_5 = random.choice(suit)
        
        # CPU Suits
        suit_6 = random.choice(suit)
        suit_7 = random.choice(suit)
        suit_8 = random.choice(suit)
        suit_9 = random.choice(suit)
        suit_10 = random.choice(suit)


        # Player Card Names
        card_1 = name_1 + " of " + suit_1
        card_2 = name_2 + " of " + suit_2
        card_3 = name_3 + " of " + suit_3
        card_4 = name_4 + " of " + suit_4
        card_5 = name_5 + " of " + suit_5
        
        # CPU Card Names
        card_6 = name_6 + " of " + suit_6
        card_7 = name_7 + " of " + suit_7
        card_8 = name_8 + " of " + suit_8
        card_9 = name_9 + " of " + suit_9
        card_10 = name_10 + " of " + suit_10


        player_hand = [card_1, card_2]
        player_total = [value_1, value_2]

        cpu_hand = [card_6, card_7]
        cpu_total = [value_6, value_7]
        
        numPlayer = sum(player_total)
        numCpu = sum(cpu_total)


        # Sets will dissolve duplicates into a single unique variable
        allCards = {card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10}
        
        # Check for Duplicates
        if len(allCards) != 10:
            continue
        else:
            break

       


def printHist(r):

    print (("[Round " + str(r) + "]").center(77, "*"))
    print ("Your hand : " + '%s' % ', '.join(map(str, player_hand)))
    print ("Python hand : " + '%s' % ', '.join(map(str, cpu_hand)))
    print ("Your score : " + str(sum(player_total)))
    print ("Python score : " + str(sum(cpu_total)))
    #print ("Bet : " + dough.bet)
    #print ("Winnings : " + 

values = {"Your hand" : player_hand,
          "Python hand" : cpu_hand,
          "Your score" : sum(player_total),
          "Python score" : sum(cpu_total),
          "Cash" : str(dough.cash)
          }

roundNo = "[Round " + str(dough.round) + "]"

history = { roundNo : values,
            }



for k, v in history.items():
        print (k.center(77, '-'))
        pprint.pprint (v)


dough.endRound()
input("lol")









    
