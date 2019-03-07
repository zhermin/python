import random
import os
from collections import Counter

# Just some starting colours. Unnecessary as I only read the initials since this is text based

RED = "R"
ORANGE = "O"
YELLOW = "Y"
GREEN = "G"
BLUE = "B"
VIOLET = "V"
all_colours = [RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET]


def check_answer():

	correct_colour = 0
	correct_position = 0

	# Use "Counter" module to get the number of letters in list for comparison
	# The module takes into account any duplicates in the lists compared to using [sets] for comparison
	# set(user_guesses).intersection(full_answer) returns only unique cases of matches

	copy_answer = full_answer.copy()

	count_ans = Counter(full_answer)
	count_user = Counter(user_guesses)
	diff = count_ans - count_user
	list_of_diff = list(diff.elements())

	for x in range (len(list_of_diff)):
		copy_answer.remove(list_of_diff[x])

	correct_colour = len(copy_answer)	
	
	for i in range (int(max_slots)):
		if user_guesses[i] == full_answer[i]:
			correct_position += 1

	return(correct_colour, correct_position)

def show_history():

	os.system("cls")
	if no_tries > 0:
		print("Guess No. / Max Tries : [Colours Guessed] - (Correct Colours, Correct Positions)\n")
		for try_no in range (no_tries):
			print("Guess No. " + str(try_no + 1) + "/" + str(max_tries) + " : [" + "] [".join(all_guesses[try_no]) + "] - " + str(all_results[try_no]))

while True: # Initialisation
	
	os.system("cls")

	no_tries = 0
	all_guesses = []
	all_results = []
	full_answer = []


	while True: # Choose Difficulty - No. Colours / Slots / Tries

		print("M A S T E R M I N D")
		print("All Colours - [RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET]\n\n")

		print("MAIN MENU\n")
		print("[0] Exit")
		print("[1] Easy (4 Colours / 4 Slots / 12 Tries)")
		print("[2] Normal (6 Colours / 4 Slots / 10 Tries)")
		print("[3] Hard (6 Colours / 5 Slots / 8 Tries)")
		print("[4] Custom")
		print("[5] Instructions")
		print("[6] About\n")
		
		difficulty = input("Choose an Option >>> ")

		if difficulty == "0": # Exit Game
			exit()

		elif difficulty == "1": # Easy (4/4/12)
			max_colours = 4
			max_slots = 4
			max_tries = 12
			os.system("cls")
			break

		elif difficulty == "2": # Normal (6/4/10)
			max_colours = 6
			max_slots = 4
			max_tries = 10
			os.system("cls")
			break

		elif difficulty == "3": # Hard (6/5/8)
			max_colours = 6
			max_slots = 5
			max_tries = 8
			os.system("cls")
			break

		elif difficulty == "4": # Custom

			os.system("cls")

			while True:
				max_colours = input("Number of Colours? (4 to 6) > ")
				if max_colours.isalpha() == True or int(max_colours) not in range (4, 7):
					os.system("cls")
					print("Type a number between 4 to 6")
					continue
				else:
					break

			os.system("cls")

			while True:
				max_slots = input("Number of Slots? (4 to 8) > ")
				if max_slots.isalpha() == True or int(max_slots) not in range (4, 9):
					os.system("cls")
					print("Type a number between 4 to 8")
					continue
				else:
					break
			
			os.system("cls")

			while True:
				max_tries = input("Maximum Number of Tries? (8 to 30) > ")
				if max_tries.isalpha() == True or int(max_tries) not in range (8, 31):
					os.system("cls")
					print("Type a number between 8 to 30")
					continue
				else:
					break

			os.system("cls")
			break

		elif difficulty == "5": # INSTRUCTIONS

			os.system("cls")
			print("INSTRUCTIONS")
			print("\n\nMastermind is a code-breaking game for two players")
			print("\nThe Codebreaker (You, the Player), tries to guess the correct pattern, in both colour and order")
			print("The Code must be deciphered within the maximum number of tries available, which is chosen at the Main Menu")
			print("The number of colours and slots available to be chosen from can also be customised from the Main Menu")
			print("\nYou can either play against the Computer, which gives you a random set of colours")
			print("Or, you can also get a Friend to choose his own desired set of colours without you looking for you to guess")
			input("\n\nPress Enter to return to the Main Menu > ")
			os.system("cls")
			continue

		elif difficulty == "6": # ABOUT

			os.system("cls")
			print("ABOUT")
			print("\n\nThis text based Mastermind game was created by Tam Zher Min in Jan 2019")
			print("\nInstagram : @zhermin_")
			print("Telegram : @zaczm")
			print("\n\nI first got the idea back in NS in the SPF where we were issued laptops with almost nothing to play around with")
			print("I then messed around with the Command Prompt and Notepad in the laptop and decided to write something fun to pass time")
			print("\nI ended up writing more or less the same game as seen here entirely in Batch")
			print("Admittedly, writing in Batch was way harder as the language was fairly limited in terms of logic-handling")
			print("Unfortunately, the files and the laptop had to be returned after I left the camp for my stint in Hougang NPC")
			print("\nI recreated this game because I used to have the physical Mastermind Board Game back when I was a child")
			print("I loved puzzles, and still do. And that is why this game still holds a place amongst the plethora of digital ones")
			print("\nThis Python file was not written optimally either, but as a self-taught beginner, I'm honestly just happy it works")
			print("Hope you found this interesting :)")
			input("\n\nPress Enter to return to the Main Menu > ")
			os.system("cls")
			continue

		else:
			os.system("cls")
			print("Type out only one number from the available options and press Enter\n")
			continue


	while True: # Choose to play against Computer or Friend

		print("Who do you want to play against?")
		print("\n[0] Exit")
		print("[1] VS Computer")
		print("[2] VS A Friend")
		print("[3] Back to Main Menu\n")
		vs_who = input("Play against? >>> ")

		if vs_who == "0": # Exit Game
			exit()

		elif vs_who == "1": # VS Computer

			for x in range (int(max_slots)): # Computer's Random Choices
				answers_index = random.randrange(int(max_colours))
				answers = all_colours[answers_index]
				full_answer.append(answers)

			break

		elif vs_who == "2": # VS A Friend

			os.system("cls")
			print("Player, don't peek! Let your friend choose their desired set of colours for you to guess!")

			while True:

				if len(full_answer) != int(max_slots):

					while True:

						full_answer_input = input("\nChoose " + str(max_slots) + " Colours! - [" + "] [".join(all_colours[:int(max_colours)]) + "] / [Z] to Undo >>> ").upper()

						if len(full_answer) > 0:

							if full_answer_input == "Z":
								del full_answer[-1]
								os.system("cls")
								print("Your Choices : [" + "] [".join(full_answer) + "]")
								continue


						if len(full_answer_input) != 1 or full_answer_input.isalpha() != True or full_answer_input not in all_colours[:int(max_colours)]:
							os.system("cls")
							print("Your Choices : [" + "] [".join(full_answer) + "]")
							print("Type only one of the letters shown")
							continue

						else:
							break

					os.system("cls")
					full_answer.append(full_answer_input)		
					print("Your Choices : [" + "] [".join(full_answer) + "]")

				else:
					break

			print("\nYou have chosen the colours : [" + "] [".join(full_answer) + "]")
			input("Press Enter to let your friend start guessing! > ")
			break

		elif vs_who == "3": # Back to Main Menu
			break

		else:
			os.system("cls")
			print("Type out only one number from the available options and press Enter\n")
			continue
	

	if vs_who == "3": # Back to Main Menu
		continue

	os.system("cls")
	print("GAME START!")

	# DEBUG : To be removed in actual game
	# print(full_answer)

	while True: # Player starts guessing

		if no_tries != int(max_tries): # Number of tries available

			user_guesses = []
			while True:

				if len(user_guesses) != len(full_answer):	# Number of positions to be guessed			

					while True:

						guess_input = input("\nGuess a Colour! - [" + "] [".join(all_colours[:int(max_colours)]) + "] / [Z] to Undo >>> ").upper()

						if len(user_guesses) > 0:

							if guess_input == "Z":
								del user_guesses[-1]
								show_history()
								print("Your Guess : [" + "] [".join(user_guesses) + "]")
								continue


						if len(guess_input) != 1 or guess_input.isalpha() != True or guess_input not in all_colours[:int(max_colours)]:
							os.system("cls")
							show_history()
							print("Your Guess : [" + "] [".join(user_guesses) + "]")
							print("Type only one of the letters shown")
							continue

						else:
							break

					show_history()

				else:
					break

				user_guesses.append(guess_input)		
				print("Your Guess : [" + "] [".join(user_guesses) + "]")
				
			if user_guesses == full_answer: # WIN!!!
				print("\nYOU WON ON GUESS NUMBER " + str(no_tries+1))
				if input("\nEnter to Restart >> ") == "":
					break

				else:
					exit()

			# Saving the 2 return values of the function "check_answer()" into a tuple (separated by commas as shortform)
			# Saves both [No. Correct Colours] and [No. Correct Positions] outside of the function

			fin_correct_colour, fin_correct_position = check_answer()
			all_results.append((fin_correct_colour, fin_correct_position))
			all_guesses.append(user_guesses)

			no_tries += 1
			show_history()

			print("\n" + str(fin_correct_colour) + " correct colour(s) but in the wrong position(s)!")
			print(str(fin_correct_position) + " correct colour(s) in the right position(s)!")

		else: # LOSE!!!
			print("\nYOU LOST!\nThe correct answer was [" + "] [".join(full_answer) + "]")
			if input("\nEnter to Restart >> ") == "":
				break

			else:
				exit()