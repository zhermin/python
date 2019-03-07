import random
import os



def main_deck():

	deck = []
	for all_cards in range (52):
		deck.append(int(all_cards))
	return deck

def draw_card(deck):

	random_card = random.choice(deck)
	deck.remove(random_card)

	chk_suit = int(random_card / 13)
	chk_value = random_card % 13 + 1

	return random_card, chk_suit, chk_value

def print_card(chk_suit, chk_value):

	all_suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
	all_values = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

	card_suit = all_suits[chk_suit]
	card_value = all_values[chk_value]

	card_text = str(card_value) + " of " + card_suit
	# print(card_text)
	return card_text
	


while True:

	deck = main_deck()

	hand = []
	table = []

	hand_suit = []
	hand_value = []
	table_suit = []
	table_value = []

	# begin drawing all the cards

	# player draw 2 cards
	print("Your Hand")
	for two_cards in range (2):
		random_card, chk_suit, chk_value = draw_card(deck)
		card_text = print_card(chk_suit, chk_value)
		hand.append(card_text)
		hand_suit.append(chk_suit)
		hand_value.append(chk_value)

	print(hand)	
	input()

	# table 5 cards
	print("The Table")
	for flop_river in range (5):
		random_card, chk_suit, chk_value = draw_card(deck)
		card_text = print_card(chk_suit, chk_value)
		table.append(card_text)
		table_suit.append(chk_suit)
		table_value.append(chk_value)

	print(table)
	input()

	total = hand + table
	total_suit = hand_suit + table_suit
	total_value = hand_value + table_value
	print(total)
	print(total_suit)
	print(total_value)
	input()




	input("\nEnd")
	os.system("cls")
