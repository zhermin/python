import random
from os import system

print ("HOW LUCKY ARE YOU???\n")

luck = input("Put in your favourite word! >>> ")
system("title " + luck)

input("Press Enter to Continue")

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def getChar():

	while True:

		ch = random.randint(0, 2)

		if ch == 0:
			opt = num
		else: 	
			opt = alpha

		char = random.choice(opt)
		
		upp = random.randint(0, 2)
		if upp == 0:
			char = char.upper()
			
		return (char)

no = 1
evth = []
	
while True:
	
	pw = ""
	i = 0

	while True:
		
		pw = pw + getChar()
		i+=1
		
		if i == 2:
		
			if pw in evth:
				print ("DUPLICATE")
				break
				
			else:		
				print (str(no) + ". " + pw)
				i+=1
				
				if i == 3:
					no+=1
		
					if pw == luck:
						print ("JACKPOTTTTTTTTTTTTTTTTTTTTTT")
						input()
						
					evth.append(pw)
					
					break
				
