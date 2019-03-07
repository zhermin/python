import random, time

deck = {"Ace" : 11, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10}
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]

class Money:

    def __init__(self):
        self.cash = 100
        self.round = 1
        self.history = {}
        self.high = {}
        self.title = {"Round Number" : "Results"}
    
    def reset(self):
        self.cash = 100
        self.round = 1
        self.history = {}
        
    def win(self, k_win):
        
        if k_win == 1:
            self.re = "DRAW"                
        elif k_win == 2:
            self.re = "WIN"
        elif k_win == 3:
            self.re = "WIN DOUBLE"
        elif k_win == 4:
            self.re = "WIN TRIPLE"
        elif k_win == 5:
            k_win -= 4
            self.re = "FREE HAND (YOU)"
        elif k_win == 6:
            k_win -=5
            self.re = "FREE HAND (CPU)"

        self.cash += self.bet * k_win

    def lose(self, k_lose):
        self.cash -= self.bet * k_lose

        if k_lose == 0:
            self.re = "LOSE"
        elif k_lose == 1:
            self.re = "LOSE DOUBLE"
        elif k_lose == 2:
            self.re = "LOSE TRIPLE"

    def checkCash(self):        
        print ("=".center(77, "="))
        print (("[Cash = $" + str(self.cash) + "]").center(77, "-"))
        print ("=".center(77, "="))

    def endRound(self): # IMPORTANT! This stores the round number and the results in the self.history dictionary
        self.history ["[Round " + str(self.round) + "]"] = self.re
        self.round += 1

    def checkRound(self):
        print ("")
        print (("[Round " + str(self.round) + "]").center(77, "*"))

    def printHist(self):
        print ("[HISTORY]".center(77, "+"))
        
        def printRe(itemsDict, leftWidth, rightWidth):
            for k, v in itemsDict.items():                
                print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
            
        printRe(self.title, 12, 65)
        print ("-".center(77, "-"))
        printRe(self.history, 60, 17)        
        print ("-".center(77, "-"))

    def saveHigh(self, name):
        h = open ("Highscores.txt", "a")
        h.write((name + " | $" + str(self.cash)).center(77))
        h.write("\n")
        h.close()

    def printHigh(self):
	
        input ("Type anything to view highscores >>> ")

        for key, value in sorted(self.high.items(), key=lambda item: (item[1], item[0])):
            print ("%s: %s" % (key, value))
            
        print ("")
        print ("[HIGHSCORES]".center(77))
        print ("~~~~~~~~~~~~~~~~".center(77))
        h = open("Highscores.txt")
        content = h.read()
        h.close()
        print (content)
        print ("-".center(77, "-"))
        
dough = Money()


def main():

    def play(comp):        

        if dough.cash < 5:
                replay()
                

        if comp == 1: # Casual
            
            while True:
                dough.checkCash()
                dough.checkRound()
                
                print ("MIN = $5 | MAX = ALL IN")
                
                try:
                    dough.bet = int(input("Place your bets! $"))
                    if dough.bet < 5:
                        print ("Please bet at least $5\n")
                        
                    elif dough.bet > dough.cash:
                        print ("Insufficient funds!")
                        print ("Click [HERE] to buy more cash!\n")
                        
                    else:
                        print ("You bet $" + str(dough.bet) + "!")
                        break
                    
                except ValueError:
                        print ("Please enter a number\n")
                        
        elif comp == 2: # Competitive

            while True:
                dough.checkCash()
                dough.checkRound()

                print ("MIN = $5 | MAX = $10")

                try:
                    dough.bet = int(input("Place your bets! $"))
                    if dough.bet < 5:
                        print ("Please bet at least $5\n")
                        
                    elif dough.bet > 10:
                        print ("You're only allowed to bet max $10!\n")
                        
                    else:
                        print ("You bet $" + str(dough.bet) + "!")
                        break
                
                except ValueError:
                    print ("Please enter a number\n")
                 
           
        dough.cash -= dough.bet
        dough.checkCash()
        
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

            # Player Starting Hand
            player_hand = [card_1, card_2]
            player_total = [value_1, value_2]
            
            # CPU Starting Hand
            cpu_hand = [card_6, card_7]
            cpu_total = [value_6, value_7]

            # Initial scores
            numPlayer = sum(player_total)
            numCpu = sum(cpu_total)
            
            # Sets will dissolve duplicates into a single unique variable
            allCards = {card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10}
            
            # Check for Duplicates
            if len(allCards) != 10:
                continue
            else:
                break


        # Cpu's turn
                
        def cpuDraw():   
                           
            while True:
                
                z = sum(cpu_total)
                d = aceCheckCpu(z)
                
                if d < z:
                    z = d

                print ("\nPython hand : " + '%s' % ', '.join(map(str, cpu_hand)))
                print ("Python Score = " + str(z))
                print ("")

                if len(cpu_hand) == 5: # Checking for 5 DRAGON - CPU
                
                    if z < 21:
                        print ("Python drew 5 DRAGON! You lose double!")
                        dough.lose(1)
                    elif z == 21:
                        print ("Python drew 5 DRAGON & scored 21! You lose triple!")
                        dough.lose(2)
                    else:
                        print ("Python busted with 5 cards!\n")
                        print ("You won double! Lucky!")
                        dough.win(3)
                        
                    replay()

                if z == 17: # 17 (50% chance of drawing another card)  
                    yn = ["yes", "no"]
                    choice = random.choice(yn)

                    if choice == "no":
                        endGame()
                
                elif z < 18: # 0 - 16
                    
                    if card_8 not in cpu_hand:
                        print ("Python drew..")
                        time.sleep(2)
                        print ("The " + card_8)
                        cpu_hand.append(card_8)
                        cpu_total.append(value_8)        
                        continue
                    else:
                        if card_9 not in cpu_hand:
                            print ("Python drew..")
                            time.sleep(2)
                            print ("The " + card_9)
                            cpu_hand.append(card_9)
                            cpu_total.append(value_9)
                            continue
                        else:
                            if card_10 not in cpu_hand:
                                print ("Python drew..")
                                time.sleep(2)
                                print ("The " + card_10)
                                cpu_hand.append(card_10)
                                cpu_total.append(value_10)
                                continue
                            
                else: # 18 - 21
                    endGame()

        # Correcting scores if hands contain ace(s)

        def aceCheckPlayer(a):
                    
            acesPlayer = list(filter(lambda item: item.startswith("Ace"), player_hand))
            
            if len(player_hand) == 3:
            
                if len(acesPlayer) == 1:
                
                    if a > 22:
                        return a - 10
                    elif a < 23:
                        return a - 1
                        
                elif len(acesPlayer) == 2:
                    return a - 11

                else:
                    return a

            elif len(player_hand) > 3:

                for i in range(len(acesPlayer)):
                    a -= 10
                return a

            else:
                return a

        def aceCheckCpu(b):
            
            acesCpu = list(filter(lambda item: item.startswith("Ace"), cpu_hand))

            if len(cpu_hand) == 3:
            
                if len(acesCpu) == 1:
                
                    if b > 22:
                        return b - 10
                    elif b < 23:
                        return b - 1
                        
                elif len(acesCpu) == 2:
                    return b - 11

                else:
                    return b

            elif len(cpu_hand) > 3:

                for i in range(len(acesCpu)):
                    b -= 10
                return b

            else:
                return b

        # Checking player's score

        def compare(c):
            
            c = aceCheckPlayer(sum(player_total))
            y = sum(player_total)

            if c < y:
                y = c
            
                
            if len(player_hand) == 5: # Checking for 5 DRAGON - Player
                
                if y < 21:
                    print ("Total Score = " + str(y))
                    print ("5 DRAGON! DOUBLE PAYOUT!")
                    dough.win(3)
                elif y == 21:
                    print ("Total Score = " + str(y))
                    print ("5 DRAGON & SCORED 21! TRIPLE PAYOUT!")
                    dough.win(4)
                else:
                    print ("Total Score = " + str(y))
                    print ("\nBUSTED!\n")
                    print ("You lose double! Unlucky!")
                    dough.lose(1)

                replay()
                
            
            if y < 16:
                return c
            
            elif y < 22:
                return c
            
            else:
                print ("Total Score = " + str(y))
                print ("Your score is above 21, hopefully Python busts as well!")
                cpuDraw()
                endGame()
                
                               
        def endGame():

            time.sleep(3)
                  
            # Replacing scores without ace(s)
            
            c = aceCheckPlayer(sum(player_total))
            y = sum(player_total)

            if c < y:
                y = c

            z = sum(cpu_total)
            d = aceCheckCpu(z)
            
            if d < z:
                z = d

            # Processing results
            
            if z > 21 and y > 21:
                print ("Python busts as well! Your bet is returned to you!")
                dough.win(1)
                
            elif z > 21:
                print ("Python busts! You win!")
                dough.win(2)
                
            elif y > 21:
                print ("BUSTED!")
                dough.lose(0)
                
            elif z > y:
                print ("You lost by " + str(z - y) + " points!")
                dough.lose(0)

            elif z < y:
                print ("You won by " + str(y - z) + " points!")
                dough.win(2)
                      
            elif y == z:
                print ("It's a draw! Your bet is returned to you!")
                dough.win(1)

            print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))
            print ("Python hand : " + '%s' % ', '.join(map(str, cpu_hand)))

            print ("\nYou scored " + str(y))
            print ("Python scored " + str(z))

            replay()
            
        # Card Dealing

        print ("You are dealt the " + card_1)
        print ("")

        time.sleep(1)

        print ("    Python was dealt the " + card_6)
        print ("")

        time.sleep(1)

        print ("You are dealt a second card, the " + card_2)
        print ("")

        time.sleep(1)

        print ("    Python was dealt a second card")
        print ("")

        print ("Your hand : " + '%s' % ', '.join(map(str, player_hand)))
        print ("")


        # Two cards check

        if numPlayer == 15: # Free Hands
            
            while True:
                cont = input("You have a free hand! Type 'in' to continue or 'out' to re-draw! ").lower()
                
                if cont == "in":
                    break
                elif cont == "out":
                    print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))
                    print ("Python hand : " + '%s' % ', '.join(map(str, cpu_hand)))

                    if sum(cpu_total) == 21:
                        print ("\nYou dodged a BAN LUCK! Lucky!")
                    elif sum(cpu_total) == 22:
                        print ("\nYou dodged a BAN BAN! Super lucky!")
                        
                    dough.win(5)    
                    replay()
                else:
                    print ("\nPlease enter either 'in' or 'out'!")
                    
        elif numCpu == 15:
            print ("Python drew a free hand!")
            time.sleep(1)
            print ("He has decided to re-draw!\n")
            print ("Your hand : " + '%s' % ', '.join(map(str, player_hand)))
            print ("Python hand : " + '%s' % ', '.join(map(str, cpu_hand)))
            dough.win(6)
            replay()


        if numPlayer > 20 and numCpu > 20 and numCpu == numPlayer: # Check for BAN LUCK / BAN BAN draws
            endGame()

        else:    
            if numPlayer == 22:
                print ("Python hand : " + '%s' % ', '.join(map(str, cpu_hand)))
                print ("\nBAN BAN! TRIPLE PAYOUT!")
                dough.win(4)
                replay()
            elif numPlayer == 21:
                print ("Python hand : " + '%s' % ', '.join(map(str, cpu_hand)))
                print ("\nBAN LUCK! DOUBLE PAYOUT!")

                if numCpu == 22:
                    print ("Python hand : " + '%s' % ', '.join(map(str, cpu_hand)))
                    print ("\nPython drew a BAN BAN! Python beat your hand! You lose triple!")
                    dough.lose(2)
                    replay()
                    
                dough.win(3)
                replay()
                
            elif numCpu == 22:
                print ("Python hand : " + '%s' % ', '.join(map(str, cpu_hand)))
                print ("\nPython drew a BAN BAN! You lose triple!")    
                dough.lose(2)
                replay()
            elif numCpu == 21:
                print ("Python hand : " + '%s' % ', '.join(map(str, cpu_hand)))
                print ("\nPython drew a BAN LUCK! You lose double!")
                dough.lose(1)
                replay()

        # No BAN LUCK / BAN BAN

        if numPlayer < 16: 
            print ("Total Score = " + str(numPlayer))
            print ("Your score is below 16! You need to hit!\n")
            inp = input("Hit? ").lower()
        elif numPlayer < 21:
            print ("Total Score = " + str(numPlayer))
            print ("You are within 21!\n")       
            inp = input("Hit or stand? ").lower()


        # Player drawing 3rd card

        while True:       

            if inp == "hit":
                player_hand.append(card_3)
                player_total.append(value_3)
                print ("You drew..")
                time.sleep(2)
                print ("The " + card_3 + "!")
                print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))
                print ("")

                if compare(sum(player_total)) < 16:
                    print ("Total Score = " + str(compare(sum(player_total))))
                    print ("Your score is below 16! You need to hit!\n")
                    inp = input("Hit? ").lower()
                    break
                
                else:
                    print ("Total Score = " + str(compare(sum(player_total))))
                    print ("You are within 21!\n")
                    inp = input ("Hit or stand? ").lower()
                    break
                
            elif inp == "stand":
                
                if compare(sum(player_total)) < 16:
                    print ("Total Score = " + str(compare(sum(player_total))))
                    print ("Your score is below 16! You need to hit!\n")
                    inp = input("Hit? ").lower()
                    continue
                
                print ("You would have drawn the " + card_3)            
                cpuDraw()
            
            else:
                print ("Please enter either hit or stand\n")
                inp = input("Hit or stand? ").lower()
                continue

        # Player drawing 4th card

        while True:       

            if inp == "hit":
                player_hand.append(card_4)
                player_total.append(value_4)
                print ("You drew..")
                time.sleep(2)
                print ("The " + card_4 + "!")
                print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))
                print ("")
                
                if compare(sum(player_total)) < 16:
                    print ("Total Score = " + str(compare(sum(player_total))))
                    print ("Your score is below 16! You need to hit!\n")
                    inp = input("Hit? ").lower()
                    break
                
                else:
                    print ("Total Score = " + str(compare(sum(player_total))))
                    print ("You are within 21!\n")
                    print ("You have 4 cards in your hand now! Busting on your next card will cause you to lose double!\n")
                    inp = input ("Hit or stand? ").lower()
                    break
                
            elif inp == "stand":

                if compare(sum(player_total)) < 16:
                    print ("Total Score = " + str(compare(sum(player_total))))
                    print ("Your score is below 16! You need to hit!\n")
                    inp = input("Hit? ").lower()
                    continue
                
                print ("You would have drawn the " + card_4)            
                cpuDraw()
            
            else:
                print ("Please enter either hit or stand\n")
                inp = input("Hit or stand? ").lower()
                continue

        # Player drawing 5th card

        while True:       

            if inp == "hit":
                player_hand.append(card_5)
                player_total.append(value_5)
                print ("You drew..")
                time.sleep(2)
                print ("The " + card_5 + "!")
                print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))
                print ("")
                compare(sum(player_total))
                
            elif inp == "stand":

                if compare(sum(player_total)) < 16:
                    print ("Total Score = " + str(compare(sum(player_total))))
                    print ("Your score is below 16! You need to hit!\n")
                    inp = input("Hit? ").lower()
                    continue
                
                print ("You would have drawn the " + card_5)
                cpuDraw()
            
            else:
                print ("Please enter either hit or stand\n")
                inp = input("Hit or stand? ").lower()
                continue

    
    # Replay game and history

    def replay():
        
        dough.checkCash()
        dough.endRound()
        
        while True:

            if comp == 2: # Competitive - End game
                
                if dough.round == 2:
  
                    while True: # Get name
                        name = input ("Enter your name! ").upper()

                        if name.isalpha() == False:
                            print ("Please enter only alphabets!\n")
                        elif len(name) < 3:
                            print ("Please enter at least 3 letters!\n")
                        elif len(name) > 4:
                            print ("Please enter at most 4 letters!\n")
                        else:
                            break
                    
                    dough.printHist()
                    dough.saveHigh(name)
                    dough.printHigh()

                    while True:
                        quitGame = input("Type anything to view match history, '/r' to play again or '/q' to quit\n>>> ").lower()
                        
                        if quitGame == "/q":
                            exit()
                        elif quitGame == "/r":
                            dough.reset()
                            main()
                        else:
                            dough.printHist()
                            dough.printHigh()

            if dough.cash < 5: # Endless
                dough.printHist()
                quitGame = input("Type anything to view match history, '/r' to play again or '/q' to quit\n>>> ").lower()

                if quitGame == "/q":
                    exit()
                elif quitGame == "/r":
                    dough.reset()
                    main()
                else:
                    print ("\nI don't know what you wrote but thanks for playing!\n")
                    continue
            else:

                print ("Type '/h' to view match history or '/r' to play again or '/q' to quit!")
                play_again = input("Press enter to play again >>> ").lower()
                
                if play_again == "":
                    play(comp) 
                elif play_again == "/h":
                    dough.printHist()
                elif play_again == "/r":
                    dough.reset()
                    main()
                elif play_again == "/q":
                    exit()
                else:
                    print ("\nI don't know what you wrote but thanks for playing!\n")
                    continue

    # Main menu

    while True:
          
        try:
            print ("[BAN LUCK]".center(77, "*"))          
            print ("Main Menu\n")
            print ("1) Endless\n2) Competitive\n3) Rules\n4) Scoring system\n5) Credits")
            comp = int(input(">>> "))
            if comp == 1:
                play(comp)
                
            elif comp == 2:
                play(comp)
                
            elif comp == 3:
                print ("*".center(77, "*"))   
                print("""Rules:

The goal is simple - draw (hit) as many cards as needed to get as close to 21
without going over (busting) to beat the computer.

However, you can only stop drawing (stand) if your total score is above 16.


Endless: Endless gameplay - until you run out of cash

Competitive: Test your luck and skill for 10 rounds to have the highest amount of cash!""")
                print ("*".center(77, "*")) 
                input ("Type anything to continue >>> ")
                continue
            
            elif comp == 4:
                print ("*".center(77, "*"))  
                print ("""Values:

10, J, Q, K = 10 points

If hand has 2 cards, Ace = 11 points
If hand has 3 cards, Ace = 10 or 1 point(s)
If hand has 4/5 cards, Ace = 1 point


Special Hands:

Initial Hand totals to 15 points = Free Hand
    >>> Able to redraw (surrender)
Ace + 10/J/Q/K = BAN LUCK
    >>> Doubles winnings/losings
Ace + Ace = BAN BAN
    >>> Triples winnings/losings
5 Cards without going bust = 5 DRAGON
    >>> Doubles winnings/losings
5 Cards + Scores 21 = 5 DRAGON
    >>> Triples winnings/losings""")
                print ("*".center(77, "*")) 
                input ("Type anything to continue >>> ")
                continue
            
            elif comp == 5:
                print ("*".center(77, "*"))
                print ("Credits:\n")
                print ("Created by Zher Min")
                print ("*".center(77, "*")) 
                input ("Type anything to continue >>> ")
                continue

            elif comp == 6:
                dough.printHigh()
                
            else:
                print ("\nPlease enter a valid option!\n")
                input ("Type anything to continue >>> ")
                continue

        except ValueError:
            print ("\nPlease enter a number!\n")



print ("Welcome to a simplified version of BAN LUCK where it's you against the computer!\n") 
print ("Unfortunately, multiplayer is not supported yet.")

main()



