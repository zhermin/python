numPlayer = sum(player_total)
numCpu = sum(cpu_total)

# CPU has 2 cards

if numCpu < 18:
    add_card_cpu = cpu_hand.append(card_8), cpu_total.append(value_8)
    print ("Python drew the " + card_8)
elif numCpu == 21 and numPlayer != 21 and len(player_hand) == 2:
    print ("Python drew a BAN LUCK! You lose double!")
elif numCpu == 22 and numPlayer != 22 and len(player_hand) == 2:
    print ("Python drew a BAN BAN! You lose triple!")
else:
    compare()
    
if numCpu < 18:
    add_card_cpu = cpu_hand.append(card_9), cpu_total.append(value_9)
    print ("Python drew the " + card_9)
else:
    compare()
    
if numCpu < 18:
    add_card_cpu = cpu_hand.append(card_10), cpu_total.append(value_10)
    print ("Python drew the " + card_10)
    if numCpu < 21:
        print ("5 DRAGON from Python! You lose double!")
    elif numCpu == 21:
        print ("5 DRAGON from Python and Score = 21! You lose triple!")
    else:
        print ("Python busts! You win double! Lucky!")
else:
    compare()
    
