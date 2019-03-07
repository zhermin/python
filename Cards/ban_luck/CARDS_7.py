import random, time, sys
sys.setrecursionlimit(10000)

# Definitions

deck = {"Ace" : 11, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10}
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]


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


hand = [card_1, card_2]
total = [value_1, value_2]



def player():
    
    while True:
        if card_1 != card_2 != card_3 != card_4 != card_5:
            break
        else:
            try:
                player()
            except RecursionError:
                print("Memory Cap Reached\n")
                return
            break


    # Card Dealing

    print ("You are dealt the " + card_1)
    print ("")



    print ("    Python was dealt a card")
    print ("")



    print ("You are dealt a second card, the " + card_2)
    print ("")
    


    print ("    Python was dealt a second card")
    print ("")
    
    print ("Your hand : " + '%s' % ', '.join(map(str, hand)))


    # Two card check - Player

    if sum(total) < 16:
        print ("Total Score = " + str(sum(total)))
        print ("Your score is below 16! You need to hit!\n")
        hit = input("Hit? ")
    elif sum(total) < 21:
        print ("Total Score = " + str(sum(total)))
        print ("")
        hit = input("Hit or stand? ")
    elif sum(total) == 22:
        print ("BAN BAN! TRIPLE PAYOUT!\n")
        return
    elif sum(total) == 21:
        print ("BAN LUCK! DOUBLE PAYOUT!\n")
        return

    # Drawing third card

    while True:       

        if hit == "hit":
            add_card = hand.append(card_3), total.append(value_3)
            print ("\nYour hand : " + '%s' % ', '.join(map(str, hand)))

            if "Ace of Spades" in hand or "Ace of Hearts" in hand or "Ace of Clubs" in hand or "Ace of Diamonds" in hand:
                if sum(total) > 22:
                    num_total = sum(total) - 10
                    print ("Since you have Ace(s) in your hand\n")
                    print ("Total Score = " + str(num_total))
                    if num_total > 21:
                        print("BUSTED!")
                        return
                    elif sum(total) < 16:
                        print ("Total Score = " + str(num_total))
                        print ("Your score is below 16! You need to hit!\n")
                        hit = input("Hit? ")
                        break
                    else:
                        print("You are within 21!\n")
                        hit = input("Hit or stand? ")
                        break
                else:
                    num_total = sum(total) - 1
                    print ("Since you have Ace(s) in your hand\n")
                    print ("Total Score = " + str(num_total))
                    if num_total > 21:
                        print("BUSTED!")
                        return
                    elif sum(total) < 16:
                        print ("Total Score = " + str(num_total))
                        print ("Your score is below 16! You need to hit!\n")
                        hit = input("Hit? ")
                        break
                    else:
                        print("You are within 21!\n")
                        hit = input("Hit or stand? ")
                        break
                        
            else:
                print ("Total Score = " + str(sum(total)))
                if sum(total) > 21:
                    print("BUSTED!")
                    return
                elif sum(total) < 16:
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


    # Drawing fourth card

    while True:       

        if hit == "hit":
            add_card = hand.append(card_4), total.append(value_4)
            print ("\nYour hand : " + '%s' % ', '.join(map(str, hand)))

            if "Ace of Spades" in hand or "Ace of Hearts" in hand or "Ace of Clubs" in hand or "Ace of Diamonds" in hand:
                if sum(total) > 22:
                    num_total = sum(total) - 10
                    print ("Since you have Ace(s) in your hand\n")
                    print ("Total Score = " + str(num_total))
                    if num_total > 21:
                        print("BUSTED!")
                        return
                    elif sum(total) < 16:
                        print ("Total Score = " + str(num_total))
                        print ("Your score is below 16! You need to hit!\n")
                        hit = input("Hit? ")
                        break
                    else:
                        print("You are within 21!\n")
                        hit = input("Hit or stand? ")
                        break

                else:
                    num_total = sum(total) - 1
                    print ("Since you have Ace(s) in your hand\n")
                    print ("Total Score = " + str(num_total))
                    if num_total > 21:
                        print("BUSTED!")
                        return
                    elif sum(total) < 16:
                        print ("Total Score = " + str(num_total))
                        print ("Your score is below 16! You need to hit!\n")
                        hit = input("Hit? ")
                        break
                    else:
                        print("You are within 21!\n")
                        hit = input("Hit or stand? ")
                        break
                        
            else:
                print ("Total Score = " + str(sum(total)))
                if sum(total) > 21:
                    print("BUSTED!")
                    return
                elif sum(total) < 16:
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
            add_card = hand.append(card_4), total.append(value_4)
            print ("\nYour hand : " + '%s' % ', '.join(map(str, hand)))

            if "Ace of Spades" in hand or "Ace of Hearts" in hand or "Ace of Clubs" in hand or "Ace of Diamonds" in hand:
                if sum(total) > 22:
                    num_total = sum(total) - 10
                    print ("Since you have Ace(s) in your hand\n")
                    print ("Total Score = " + str(num_total))
                    if num_total > 21:
                        print("BUSTED!")
                        print("You lose triple! Unlucky!")
                        return
                    else:
                        print("5 DRAGON! TRIPLE PAYOUT!\n")
                        return
                else:
                    num_total = sum(total) - 1
                    print ("Since you have Ace(s) in your hand\n")
                    print ("Total Score = " + str(num_total))
                    if num_total > 21:
                        print("BUSTED!\n")
                        print("You lose triple! Unlucky!")
                        return
                    else:
                        print("5 DRAGON! TRIPLE PAYOUT!\n")
                        return
            else:
                print ("Total Score = " + str(sum(total)))
                if sum(total) > 21:
                    print("BUSTED!")
                    print("You lose triple! Unlucky!")
                    return
                else:
                    print("5 DRAGON! TRIPLE PAYOUT!\n")
                    return

        elif hit == "stand":
            compare()
            return
        else:
            return




def compare():
    CPU = random.randint(16,25)
    if CPU > 21 :
        print("Python busts! You win!")
    elif CPU > sum(total):
        print("You lost by " + str(CPU - sum(total)))
    elif sum(total) == CPU:
        print("It's a draw!")  
    else:
        print("You won by " + str(sum(total) - CPU))

    print ("\nPython has a total score of " + str(CPU))


        


player()
