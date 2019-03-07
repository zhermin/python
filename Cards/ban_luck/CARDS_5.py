class Card:
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    RANKS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King')

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):

        return '{0} of {1}'.format(Card.RANKS[self.rank],
                                   Card.SUITS[self.suit])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
