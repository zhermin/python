import random

z = 17

if z == 17: # 17  
    yn = ["yes", "no"]
    choice = random.choice(yn)

    if choice == "yes":
        pass
    else:
        print ("endgame")
        exit()

if z < 18:
    print ("hi")
    print ("drawing some cards")

else:
    print ("endgame")
    exit()
