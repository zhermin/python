import random
def play():

    def pboard(board):
        for i in board:
            print(i)
        print()

    board = [[0 for c in range(4)] for r in range(4)]
    board = [[2,2,0,4],[2,0,0,0],[0,2,2,4],[2,4,2,2]]
    #pboard(board)

    try:
        spawn = random.choice([(r,c) for r in range(len(board)) for c in range(len(board[r])) if board[r][c] == 0])
        board[spawn[0]][spawn[1]] = 2
    except IndexError:
        pboard(board)
        print("GAME OVER")
        return

    pboard(board)

    def left(board):
        for r in range(len(board)):
            for c in range(1,len(board)-1):
                board[r] = [i for i in board[r] if i!=0] + [j for j in board[r] if j==0]
                if board[r][c-1] == board[r][c]:
                    board[r][c-1] += board[r][c]
                    board[r][c] = 0

                if board[r][c] == board[r][c+1]:
                    board[r][c] += board[r][c+1]
                    board[r][c+1] = 0
                board[r] = [i for i in board[r] if i!=0] + [j for j in board[r] if j==0]
        return board

    def right(board):
        return [r[::-1] for r in left([r[::-1] for r in board])]

    def up(board):
        return [list(i) for i in zip(*left([list(i) for i in zip(*board)]))]

    def down(board):
        return [list(i) for i in zip(*right([list(i) for i in zip(*board)]))]

    board = down(board)
    pboard(board)

#play()

class Board:

    def __init__(self):
        self.board = [[0 for c in range(4)] for r in range(4)]
        self.board = [[2,2,0,4],[2,0,0,0],[0,2,2,4],[2,4,2,2]]

    def play(self):
        #self.pboard()
        while True:
            gameover = self.spawn_tile()
            if gameover:
                return
            self.pboard()
            self.right()
            self.pboard()
            input('CONTINUE')

    def spawn_tile(self):
        try:
            spawn = random.choice([(r,c) for r in range(len(self.board)) for c in range(len(self.board[r])) if self.board[r][c] == 0])
            self.board[spawn[0]][spawn[1]] = 2
        except IndexError:
            self.pboard()
            print("GAME OVER")
            return True

    def pboard(self):
        for i in self.board:
            print(i)
        print()

    def left(self):
        for r in range(len(self.board)):
            for c in range(1,len(self.board)-1):
                self.board[r] = [i for i in self.board[r] if i!=0] + [j for j in self.board[r] if j==0]
                if self.board[r][c-1] == self.board[r][c]:
                    self.board[r][c-1] += self.board[r][c]
                    self.board[r][c] = 0

                if self.board[r][c] == self.board[r][c+1]:
                    self.board[r][c] += self.board[r][c+1]
                    self.board[r][c+1] = 0
                self.board[r] = [i for i in self.board[r] if i!=0] + [j for j in self.board[r] if j==0]

    def right(self):
        self.board = [r[::-1] for r in self.board]
        self.left()
        self.board = [r[::-1] for r in self.board]
        # return board
        # self.board = [r[::-1] for r in self.left([r[::-1] for r in self.board])]

    def up(self):
        return [list(i) for i in zip(*self.left([list(i) for i in zip(*self.board)]))]

    def down(self):
        return [list(i) for i in zip(*self.right([list(i) for i in zip(*self.board)]))]

myboard = Board()
myboard.play()