import random
import itertools
SUITS = 'cdhs'
RANKS = '23456789TJQKA'
DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
hand = random.sample(DECK, 5)
print (hand)

print ("your card is %s%s" % (SUITS, RANKS))
