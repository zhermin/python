import random



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

while True:    

    if name_1 == name_2 == name_3 == name_4 == name_5 and suit_1 == suit_2 == suit_3 == suit_4 == suit_5:
        name_2, value_2 = random.choice (list(deck.items()))
        name_3, value_3 = random.choice (list(deck.items()))
        name_4, value_4 = random.choice (list(deck.items()))
        name_5, value_5 = random.choice (list(deck.items()))
        
        suit_2 = random.choice(suit)
        suit_3 = random.choice(suit)
        suit_4 = random.choice(suit)
        suit_5 = random.choice(suit)
    else:
        print ("Your hand : " + '%s' % ', '.join(map(str, hand)))
        print ("")
        break

    


def hit():

    
    hand = [card_1, card_2]
    total = [value_1, value_2]

    
    hit = input("Hit or stand? ")
    while True:       
        if hit == "hit":
            add_card = hand.append(card_3), total.append(value_3)
            print ("You drew : " + '%s' % ', '.join(map(str, hand)))
            print ("Total Score = " + str(sum(total)))
            if sum(total) > 21:
                print("BUSTED!")
                exit()
            else:
                print("You are within 21!")
                input("Hit or stand? ")
                break
                    
        elif hit == "stand":
            exit()
        else:
            print("Please enter either hit or stand")
            hit = input("Hit or stand? ")

    if "Ace of Spades" in hand or "Ace of Hearts" in hand or "Ace of Clubs" in hand or "Ace of Diamonds" in hand:
        if sum(total) > 21:
            total = sum(total) - 10
            print ("Since you have an Ace in your hand")
            print ("Total Score = " + str(total))
        elif sum(total) == 22:
            total = sum(total) - 1
            print ("Since you have an Ace in your hand")
            print ("Total Score = " + str(total))
        else:
            total = sum(total) - 1
            print ("Since you have an Ace in your hand")
            print ("Total Score = " + str(total))

            
            
      


    while True:       
        if hit == "hit":
            add_card = hand.append(card_4), total.append(value_4)
            print ("You drew : " + '%s' % ', '.join(map(str, hand)))
            print ("Total Score = " + str(sum(total)))
            if sum(total) > 21:
                print("BUSTED!")
                exit()
            else:
                print("You are within 21!")
                input("Hit or stand? ")
                break

            if "Ace of Spades" in hand or "Ace of Hearts" in hand or "Ace of Clubs" in hand or "Ace of Diamonds" in hand:
                if sum(total) > 21:
                    total = sum(total) - 10
                    print ("Since you have an Ace in your hand")
                    print ("Total Score = " + str(total))
                elif sum(total) == 22:
                    total = sum(total) - 1
                    print ("Since you have an Ace in your hand")
                    print ("Total Score = " + str(total))
                else:
                    total = sum(total) - 1
                    print ("Since you have an Ace in your hand")
                    print ("Total Score = " + str(total))
                    
        elif hit == "stand":
            exit()
        else:
            print("Please enter either hit or stand")
            hit = input("Hit or stand? ")



    while True:       
        if hit == "hit":
            add_card = hand.append(card_5), total.append(value_5)
            print ("You drew : " + '%s' % ', '.join(map(str, hand)))
            print ("Total Score = " + str(sum(total)))
            if sum(total) > 21:
                print("BUSTED!")
                exit()
            else:
                print("DRAGON! TRIPLE PAYOUT!")
                exit()

            if "Ace of Spades" in hand or "Ace of Hearts" in hand or "Ace of Clubs" in hand or "Ace of Diamonds" in hand:
                if sum(total) > 21:
                    total = sum(total) - 10
                    print ("Since you have an Ace in your hand")
                    print ("Total Score = " + str(total))
                    print("DRAGON! TRIPLE PAYOUT!")
                    exit()
                elif sum(total) == 22:
                    total = sum(total) - 1
                    print ("Since you have an Ace in your hand")
                    print ("Total Score = " + str(total))
                else:
                    total = sum(total) - 1
                    print ("Since you have an Ace in your hand")
                    print ("Total Score = " + str(total))
                    
        elif hit == "stand":
            exit()
        else:
            print("Please enter either hit or stand")
            hit = input("Hit or stand? ")







if sum(total) < 17:
    print ("Total Score = " + str(sum(total)))
    print ("Your score is below 16! You need to hit!\n")
    hit()
elif sum(total) < 21:
    print ("Total Score = " + str(sum(total)))
    print ("")
    hit()
elif sum(total) == 22:
    print ("\nBAN BAN! TRIPLE PAYOUT!\n")
else:
    print ("\nBAN LUCK! DOUBLE PAYOUT!\n")





    
