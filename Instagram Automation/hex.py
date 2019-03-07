import random, time
from os import system
z
system ("title " + "Hex Code Randomiser")
print ("Hex Code Randomiser")
print ("(Actually just a really trashy python file cuz I'm bored)\n")
input ("Press Enter to Start > ")

digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

while True:
    
    hex_code = "******"

    for i in hex_code:
        
        res = random.choice(digit)                                    
        hex_code = hex_code.replace("*", res, 1)
        print ("\n" + hex_code)
        system ("title " + hex_code)
        time.sleep(1.5)

    input ("\nYour Lucky Hex Code : " + hex_code)

    restart = input ("\nType R to Restart > ")
    if str.lower(restart) == "r":
        continue
    else:
        break
