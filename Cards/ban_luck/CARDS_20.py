class Money:

    def __init__(self):
        self.cash = 100

    def reset(self):
        self.cash = 100

    def win(self, k_win):
        self.cash += k_win * 10


dough = Money()

print (dough.cash)

dough.win(1)

print (dough.cash)

dough.reset()

print (dough.cash)
