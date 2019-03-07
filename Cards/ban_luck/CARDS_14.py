player_hand = ["Ace of Spades", "5 of Spades", "Ace of Clubs", "Ace of Diamonds"]
player_total = [11, 5, 11, 11]

#Original score = 11 + 5 + 11 + 10 = 37
#Current score = 37 - 10 = 27
#Expected score = 1 + 5 + 1 + 10 = 17


print(sum(player_total))
numPlayer = sum(player_total)



aces = list(filter(lambda item: item.startswith("Ace"), player_hand))


def ace():
    global numPlayer
    if len(player_hand) == 3:

        if len(aces) == 1:
            numPlayer -= 1
            if numPlayer > 21:
                numPlayer -= 9
        elif len(aces) == 2:
            numPlayer -= 11

    elif len(player_hand) > 3:

        for i in range(len(aces)):
            numPlayer -= 10

    print(numPlayer)


ace()

"""  
    acePlayer -= 1
    if acePlayer > 22:
        acePlayer -= 10
        print ("Since you have Ace(s) in your hand\n")
        print ("Total Score = " + str(acePlayer))
        if acePlayer > 21:
            continue
            
        elif acePlayer < 16:
            print ("Your score is below 16! You need to hit!\n")
            hit = input("Hit? ")
            break
        else:
            print("You are within 21!\n")
            hit = input("Hit or stand? ")
            break

    elif acePlayer < 22:    
        acePlayer -= 1
        print ("Since you have Ace(s) in your hand\n")
        print ("Total Score = " + str(acePlayer))
        if acePlayer > 21:
            continue
            
        elif acePlayer < 16:
            print ("Your score is below 16! You need to hit!\n")
            hit = input("Hit? ")
            break
        else:
            print("You are within 21!\n")
            hit = input("Hit or stand? ")
            break
"""




