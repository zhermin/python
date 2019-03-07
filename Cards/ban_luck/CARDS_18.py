import random

# Amount of money - Player

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

def play():

    dough.bet = int(input("Place your bets! "))
    dough.cash -= dough.bet
    dough.checkCash()
    dough.checkRound()

    a = random.randint(0,6)
    if a == 1:
        print("You win!")
        dough.win(2)
    elif a == 2:
        print ("You win double!")
        dough.win(3)
    elif a == 3:
        print ("You win triple!")
        dough.win(4)
    elif a == 4:
        print("You lose!")
        dough.lose(0)
    elif a == 5:
        print ("You lose double!")
        dough.lose(1)
    elif a == 6:
        print ("You lose triple!")
        dough.lose(2)
    else:
        print ("It's a draw!")
        dough.win(1)
        
    dough.checkCash()
    dough.endRound()


def History():
    
    print ("[HISTORY]".center(77, "-"))

    def printPicnic(itemsDict, leftWidth, rightWidth):
          
        for k, v in itemsDict.items():
            print(k.ljust(leftWidth, ' ') + str(v).rjust(rightWidth))
            



    title = {"Round Number" : "Results"}
    history = {("Round " + str(dough.round)) : "WIN"}


    printPicnic(title, 35, 42)
    print ("-".center(77, "-"))
    printPicnic(history, 35, 42)





    print ("")












while True:
    play()
    history()
    history[dough.round] = "LOSE"
