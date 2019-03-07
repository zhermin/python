print ("HOW TO WHACK 101\n")

class main(object):

	def __init__(self):
		
		self.round = 0
		self.hist = [0, 0, 0, 0, 0, 0]
		
		while True:
		
			try:
				self.icash = float(format(float(input("\nCash? $")), ".2f"))
				self.cash = self.icash
				self.hist[1] = self.icash
				
				if self.icash > 0:
					print ("Your total amount is $" + str(self.icash))
					break
				else:
					print ("Please enter any number above 0")
				
			except ValueError:
				print ("Please enter a number")
				
		while True:
		
			try:
				self.pft = float(format(float(input("\n% Profit? ")), ".2f"))	
				
				if self.pft > 100:
					print ("Are you hacking??")
				elif self.pft >= 0:
					print ("The profit you are earning is " + str(self.pft) + "%")
					break
				else:
					print ("Please enter any number above 0")
				
			except ValueError:
				print ("Please enter a number")
		
		self.histTxt = open("History.txt", "w+")
		self.histTxt.write(("-" * 27) + "HISTORY | %PROFITS = " + str(self.pft) + "%" + ("-" * (31 - len(str(self.pft)))))
		self.histTxt.write("No. Cash               Whack               XPft          W/L  FCash           \n")
		self.histTxt.write("-" * 80)
		self.histTxt.close()
		

setup = main()

def printHist():

	histTxt = open("History.txt", "r")
	content = histTxt.read()
	print (content)
		
while True: # MAIN MENU
	
	while True:
	
		print ("\n\nMAIN MENU")
		opt = input("[0] Restart\n[1] Desired profits\n[2] Desired amount\n[3] Just whack\n[4] History\n>>> ")
		
		if opt == "0":

			print ("\n\n")
			setup = main()
					
		elif opt == "1":
		
			while True:
		
				try:
					dpft = float(format(float(input("\nWhat's your desired profits? $")), ".2f"))
					wdpft = float(format(dpft*setup.pft/100, ".2f"))
					
					if dpft >= 0:
						print ("To profit $" + str(dpft) + ", you need to whack $" + str(wdpft))
						break
					else:
						print ("Please enter a number that's 0 or higher")
					
				except ValueError:
					print ("Please enter a number")
			
			break
			
		elif opt == "2":
	
			while True:
		
				try:
					damt = float(format(float(input("\nWhat's your desired amount? $")), ".2f"))
					wdamt = float(format((damt-setup.cash)/setup.pft*100, ".2f"))
					
					if wdamt > setup.cash:
						print ("You wouldn't have enough to whack, the highest amount you can reach is $" + str(setup.cash*setup.pft/100))					
					elif damt > setup.cash:
						print ("To achieve $" + str(damt) + ", you need to whack $" + str(wdamt))
						break
					else:
						print ("Please ensure that you're profiting")
					
				except ValueError:
					print ("Please enter a number")
			
			break
			
		elif opt == "3":
			break
		
		elif opt == "4":
			print ("\n")
			printHist()
			input("Press any key to continue >>>")
			
		else:
			print ("Please enter a number from 0 - 4")
			continue
	
	setup.hist[1] = setup.cash
	setup.round += 1
	setup.hist[0] = setup.round
	
	while True:
	
		try:
			whack = float(format(float(input("\nWhack? $")), ".2f"))
			setup.hist[2] = whack
			
			if whack > setup.cash:
				print ("Please make sure you have enough to whack")
			elif whack >= 0:
				break
			else:
				print ("Please enter a number that's 0 or higher")

		except ValueError:
			print ("Please enter a number")

		
		
		
	if setup.icash < setup.cash:
		setup.icash = setup.cash


	print ("You are going to whack $" + str(whack))

	xpft = float(format(whack*setup.pft/100, ".2f"))
	setup.hist[3] = xpft
	print ("You will profit $" + str(xpft))

	rslt = input("\n[0] Lose or [1] Win? ")	

	while True:
	
		if rslt == "1":
			
			setup.cash = float(format(setup.cash + xpft, ".2f"))
			setup.hist[4] = "W"	
			
			print ("\nYour total profits amount to $" + str(xpft))
			print ("Your total cash is now $" + str(setup.cash))
			break

		elif rslt == "0":

			setup.cash = float(format(setup.cash - whack, ".2f"))
			setup.hist[4] = "L"
			setup.hist[5] = setup.cash

			twhack = float(format(setup.icash - setup.cash, ".2f"))
			bkev = float(format(twhack/setup.pft*100, ".2f"))
			db = float(format((2*whack*setup.pft/100-whack)/2/whack*100, ".2f"))

			print ("\nYour total loss amounts to $" + str(whack))
			print ("Your total cash is now $" + str(setup.cash))
			print ("\nTo breakeven, you need to whack $" + str(bkev))
			#print ("If you whack double, you will earn " + str(db) + "%" + " in profits relative to your last whack")

			if bkev > whack*2:
				print ("You need to whack more than double to breakeven!")
				
			
			while True:
			
				try:
					rpft = float(input("\nWhat's your desired real profits after breakeven? $"))
					fpft = twhack + rpft
					wpft = float(format(fpft/setup.pft*100, ".2f"))
					
					if rpft > 0:
						print ("\nTo achieve $" + str(rpft) + " in real profits, " + "you need to whack $" + str(wpft))
						print ("Your final amount would be $" + str(setup.cash + fpft))
						break
					elif rpft == 0:
						print ("Your final amount would be $" + str(setup.cash + twhack) + ", breaking even")
						break
					else:
						print ("Please enter a number that's 0 or higher")
					
				except ValueError:
					print ("Please enter a number")
	
			break
	
		else:
			print ("\nPlease type either 1 or 2")
			rslt = input("[0] Lose or [1] Win? ")
	
	setup.hist[5] = setup.cash
	
	setup.histTxt = open("History.txt", "a")
	
	setup.histTxt.write(str(setup.hist[0]) + "   ")
	setup.histTxt.write("$" + str(setup.hist[1]) + (" " * (19-1-len(str(setup.hist[1])))))
	setup.histTxt.write("$" + str(setup.hist[2]) + (" " * (20-1-len(str(setup.hist[2])))))
	setup.histTxt.write("$" + str(setup.hist[3]) + (" " * (14-1-len(str(setup.hist[3])))))
	setup.histTxt.write(str(setup.hist[4]) + "    ")
	setup.histTxt.write("$" + str(setup.hist[5]))
	setup.histTxt.write("\n")
	
	#setup.histTxt.write(str(setup.hist) + "\n")
	setup.histTxt.close()
	
	continue