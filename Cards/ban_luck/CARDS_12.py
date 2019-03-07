import random, time

'''
BAN LUCK
'''





# Definitions

deck = {"Ace" : 11, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10}
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]

def main():
    
    def hands():
        player_hand = [card_1, card_2]
        player_total = [value_1, value_2]

        cpu_hand = [card_6, card_7]
        cpu_total = [value_6, value_7]


    def compare():

        numPlayer = sum(player_total)
        numCpu = sum(cpu_total)
        
        if "Ace of Spades" in player_hand or "Ace of Hearts" in player_hand or "Ace of Clubs" in player_hand or "Ace of Diamonds" in player_hand:
            acePlayer = sum(player_total)
                
            if acePlayer < numPlayer:
                numPlayer = acePlayer
            else:
                pass
        
        if numCpu > 21:
            print ("Python busts! You win!")

        elif numPlayer > 21:
            print ("BUSTED!")

        elif numPlayer > 21 and numCpu > 21:
            print ("Python busts as well! It's a draw!")
            
        elif numCpu > numPlayer:
            print ("You lost by " + str(numCpu - numPlayer))

        elif numCpu < numPlayer:
            print ("You won by " + str(numPlayer - numCpu))
                  
        elif numPlayer == numCpu:
            print ("It's a draw!")

        
        print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))
        print ("Python hand : " + '%s' % ', '.join(map(str, cpu_hand)))

        print ("\nYou scored " + str(numPlayer))
        print ("Python scored " + str(numCpu))





    
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

        
        # Check for Duplicates
        if card_1 != card_2 != card_3 != card_4 != card_5 != card_6 != card_7 != card_8 != card_9 != card_10:
            break
        else:
            continue



    hands()


    
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


    # Two card check - Player

    if sum(player_total) < 16:
        print ("Total Score = " + str(sum(player_total)))
        print ("Your score is below 16! You need to hit!\n")
        hit = input("Hit? ")
    elif sum(player_total) < 21:
        print ("Total Score = " + str(sum(player_total)))
        print ("")
        hit = input("Hit or stand? ")
    elif sum(player_total) == 22:
        print ("BAN BAN! TRIPLE PAYOUT!\n")
        return
    elif sum(player_total) == 21:
        print ("BAN LUCK! DOUBLE PAYOUT!\n")
        return


    # Drawing third card - Player

    while True:       

        if hit == "hit":
            add_card = player_hand.append(card_3), player_total.append(value_3)
            print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))

            if "Ace of Spades" in player_hand or "Ace of Hearts" in player_hand or "Ace of Clubs" in player_hand or "Ace of Diamonds" in player_hand:
                acePlayer = sum(player_total)
                if acePlayer > 21:
                    acePlayer -= 10
                    print ("Since you have Ace(s) in your hand\n")
                    print ("Total Score = " + str(acePlayer))
                    if acePlayer > 21:
                        compare()
                        return
                    elif acePlayer < 16:
                        print ("Your score is below 16! You need to hit!\n")
                        hit = input("Hit? ")
                        break
                    else:
                        print("You are within 21!\n")
                        hit = input("Hit or stand? ")
                        break
                else:
                    acePlayer -= 1
                    print ("Since you have Ace(s) in your hand\n")
                    print ("Total Score = " + str(acePlayer))
                    if acePlayer > 21:
                        compare()
                        return
                    elif acePlayer < 16:
                        print ("Your score is below 16! You need to hit!\n")
                        hit = input("Hit? ")
                        break
                    else:
                        print("You are within 21!\n")
                        hit = input("Hit or stand? ")
                        break
                        
            else:
                print ("Total Score = " + str(sum(player_total)))
                if sum(player_total) > 21:
                    compare()
                    return
                elif sum(player_total) < 16:
                        print ("Your score is below 16! You need to hit!\n")
                        hit = input("Hit? ")
                        break
                else:
                    print("You are within 21!\n")
                    hit = input("Hit or stand? ")
                    break

        elif hit == "stand":
            compare()
            return
        else:
            print("Please enter either hit or stand")
            hit = input("Hit or stand? ")
            break

    # Drawing fourth card - Player

    while True:       

        if hit == "hit":
            add_card = player_hand.append(card_4), player_total.append(value_4)
            print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))

            if "Ace of Spades" in player_hand or "Ace of Hearts" in player_hand or "Ace of Clubs" in player_hand or "Ace of Diamonds" in player_hand:
                acePlayer = sum(player_total)
                if acePlayer > 21:
                    acePlayer -= 10
                    print ("Since you have Ace(s) in your hand\n")
                    print ("Total Score = " + str(acePlayer))
                    if acePlayer > 21:
                        compare()
                        return
                    elif acePlayer < 16:
                        print ("Your score is below 16! You need to hit!\n")
                        hit = input("Hit? ")
                        break
                    else:
                        print("You are within 21!\n")
                        hit = input("Hit or stand? ")
                        break
                else:
                    acePlayer -= 1
                    print ("Since you have Ace(s) in your hand\n")
                    print ("Total Score = " + str(acePlayer))
                    if acePlayer > 21:
                        compare()
                        return
                    elif acePlayer < 16:
                        print ("Your score is below 16! You need to hit!\n")
                        hit = input("Hit? ")
                        break
                    else:
                        print("You are within 21!\n")
                        hit = input("Hit or stand? ")
                        break
                        
            else:
                print ("Total Score = " + str(sum(player_total)))
                if sum(player_total) > 21:
                    compare()
                    return
                elif sum(player_total) < 16:
                        print ("Your score is below 16! You need to hit!\n")
                        hit = input("Hit? ")
                        break
                else:
                    print("You are within 21!\n")
                    hit = input("Hit or stand? ")
                    break

        elif hit == "stand":
            compare()
            return
        else:
            print("Please enter either hit or stand")
            hit = input("Hit or stand? ")
            break


    # Drawing fifth card

    while True:       

        if hit == "hit":
            add_card = player_hand.append(card_5), player_total.append(value_5)
            print ("\nYour hand : " + '%s' % ', '.join(map(str, player_hand)))

            if "Ace of Spades" in player_hand or "Ace of Hearts" in player_hand or "Ace of Clubs" in player_hand or "Ace of Diamonds" in player_hand:
                acePlayer = sum(player_total)
                if acePlayer > 21:
                    acePlayer -= 10
                    print ("Since you have Ace(s) in your hand\n")
                    print ("Total Score = " + str(acePlayer))
                    if acePlayer > 21:
                        compare()
                        print("You lose double! Unlucky!")
                        return
                    elif acePlayer == 21:
                        print("5 DRAGON and Score = 21! TRIPLE PAYOUT!\n")
                        return
                    else:
                        print("5 DRAGON! DOUBLE PAYOUT!\n")
                        return
                else:
                    acePlayer -= 1
                    print ("Since you have Ace(s) in your hand\n")
                    print ("Total Score = " + str(acePlayer))
                    if acePlayer > 21:
                        compare()
                        print("You lose double! Unlucky!")
                        return
                    elif acePlayer == 21:
                        print("5 DRAGON and Score = 21! TRIPLE PAYOUT!\n")
                        return
                    else:
                        print("5 DRAGON! DOUBLE PAYOUT!\n")
                        return
            else:
                print ("Total Score = " + str(sum(player_total)))
                if sum(player_total) > 21:
                    compare()
                    print("You lose double! Unlucky!")
                    return
                elif sum(player_total) == 21:
                    print("5 DRAGON and Score = 21! TRIPLE PAYOUT!\n")
                    return
                else:
                    print("5 DRAGON! DOUBLE PAYOUT!\n")
                    return

        elif hit == "stand":
            compare()
            return
        else:
            return


    # Drawing third card - CPU











        
main()



