import random
import os
from collections import Counter

class Cards(object):

	def __init__(self, deck, no_cards):

		self.deck = deck
		self.no_cards = no_cards

		self.hand_cards = []
		self.hand_cards_text = []

		self.hand_suit = []
		self.hand_value = []
		
		for i in range (self.no_cards): # randomise and pick no_cards(int) cards

			self.random_card = random.choice(self.deck)
			self.hand_cards.append(self.random_card)
			self.deck.remove(self.random_card)
		
			self.chk_suit = int(self.random_card / 13)
			self.hand_suit.append(self.chk_suit)

			self.chk_value = self.random_card % 13 + 1
			self.hand_value.append(self.chk_value)


			self.all_suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
			self.all_values = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

			#self.card_suit = self.all_suits[self.chk_suit]
			#self.card_value = self.all_values[self.chk_value]

			self.hand_cards_text.append( str(self.all_values[self.chk_value]) + " of " + self.all_suits[self.chk_suit]	)


	def __str__(self):

		return str(self.hand_cards_text)


	def compare(self, compare_suit, compare_value):

		self.total_suits = self.hand_suit + compare_suit
		self.total_value = self.hand_value + compare_value

		self.count_suits = Counter(self.total_suits)
		self.count_values = Counter(self.total_value)

		self.sorted_values = sorted(self.total_value)


		for same_suit in range (4):

			if self.count_suits[same_suit] == 5:
				return "Flush : {}".format(self.all_suits[same_suit])


			for i in range (len(self.sorted_values) - 4):

				strt = 0
				strt_draw = [self.sorted_values[i]]

				for x in range(4):

					#print(self.sorted_values[i], self.sorted_values[i + x + 1])
					if self.sorted_values[i] + x + 1 == self.sorted_values[i + x + 1]:
						strt += 1
						strt_draw.append(self.sorted_values[i + x + 1])

				if strt == 4:
					return "Straight Draw : {}".format(strt_draw)


		full_house = []

		for same_value in range (14):

			if self.count_values[same_value] == 4:
				full_house.extend([self.all_values[same_value]]*4)
				print("A Four of a Kind : {}".format(full_house))

			if self.count_values[same_value] == 3:
				full_house.extend([self.all_values[same_value]]*3)
				print("A Three of a Kind : {}".format(full_house))
				
			if self.count_values[same_value] == 2:
				full_house.extend([self.all_values[same_value]]*2)
				print("A Pair : {}".format(self.all_values[same_value]))

		if len(full_house) == 5:
			return "Full House : {}".format(full_house)


def main_deck():

	deck = []
	for all_cards in range (52):
		deck.append(int(all_cards))
	return deck



while True:

	deck = main_deck()
	player_one = Cards(deck, 2)
	table = Cards(deck, 5)

	print(player_one)
	print(table)
	input()

	print(player_one.compare(table.hand_suit, table.hand_value))
	input()


