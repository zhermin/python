import random, time




deck = {"Ace" : 11, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10}
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]


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
    
    # Check for Duplicates
    if card_1 != card_2 != card_3 != card_4 != card_5 != card_6 != card_7 != card_8 != card_9 != card_10:
        break
    else:
        continue


        


    
def main():
          

    def aceCheck(t):
            
        aces = list(filter(lambda item: item.startswith("Ace"), player_hand))

        print (player_hand)
        
        if len(player_hand) == 3:
        
            if len(aces) == 1:
            
                if t > 22:
                    return t - 10
                elif t < 23:
                    return t - 1
                    
            elif len(aces) == 2:
                return t - 11

        elif len(player_hand) > 3:

            for i in range(len(aces)):
                return t - 10
               
       
    def compare(t1):
    
        d = aceCheck(sum(player_total))
        
        z = sum(player_total)

        if d < sum(player_total):
            z = d
        
        if z < 16:
            print ("Total Score = " + str(z))
            print ("Your score is below 16! You need to hit!\n")
            hit = input("Hit? ")
            return
        elif z < 22:
            print ("Total Score = " + str(z))
            print ("You are within 21!\n")
            hit = input("Hit or stand? ")
            return
        else:
            endGame()


            
    def endGame():
   
        if numCpu > 21:
            print ("Python busts! You win!")

        elif sum(player_total) > 21:
            print ("BUSTED!")

        elif sum(player_total) > 21 and numCpu > 21:
            print ("Python busts as well! It's a draw!")
            
        elif numCpu > sum(player_total):
            print ("You lost by " + str(numCpu - sum(player_total)))

        elif numCpu < sum(player_total):
            print ("You won by " + str(sum(player_total) - numCpu))
                  
        elif sum(player_total) == numCpu:
            print ("It's a draw!")

        print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))
        print ("Python hand : " + '%s' % ', '.join(map(str, cpu_hand)))

        print ("\nYou scored " + str(sum(player_total)))
        print ("Python scored " + str(numCpu))

        exit()
        




        
    
    # Card Dealing

    print ("You are dealt the " + card_1)
    print ("")



    print ("    Python was dealt the " + card_6)
    print ("")



    print ("You are dealt a second card, the " + card_2)
    print ("")
    


    print ("    Python was dealt a second card")
    print ("")
    
    print ("Your hand : " + '%s' % ', '.join(map(str, player_hand)))
    print ("")


    # Two card check - Player

    if sum(player_total) < 16:
        print ("Total Score = " + str(sum(player_total)))
        print ("Your score is below 16! You need to hit!\n")
        hit = input("Hit? ")
    elif sum(player_total) < 21:
        print ("Total Score = " + str(sum(player_total)))
        print ("You are within 21!\n")       
        hit = input("Hit or stand? ")
    elif sum(player_total) == 22:
        print ("BAN BAN! TRIPLE PAYOUT!\n")
        return
    elif sum(player_total) == 21:
        print ("BAN LUCK! DOUBLE PAYOUT!\n")
        return







    # Drawing 3rd card

    t1 = compare(sum(player_total))

    while True:       

        if hit == "hit":
            player_hand.append(card_3)
            player_total.append(value_3)
            print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))
            print ("Total Score = " + str(t1))
            print ("")
            compare()
            break
            
        elif hit == "stand":
            endGame()
            return
        
        else:
            print("Please enter either hit or stand")
            hit = input("Hit or stand? ")
            break


    # Drawing 4th card

    t2 = compare(sum(player_total))

    while True:       
    
        if hit == "hit":
            player_hand.append(card_4)
            player_total.append(value_4)
            print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))
            print ("Total Score = " + str(t2))
            print ("")
            compare()
            break
            
        elif hit == "stand":
            endGame()
            return
        
        else:
            print("Please enter either hit or stand")
            hit = input("Hit or stand? ")
            break


    # Drawing 5th card

    while True:       

        if hit == "hit":
            player_hand.append(card_5)
            player_total.append(value_5)
            print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))
            print ("Total Score = " + str(sum(player_total)))
            print ("")
            compare()
            return
            
        elif hit == "stand":
            endGame()
            return
        
        else:
            endGame()
            return




    








    
main()





