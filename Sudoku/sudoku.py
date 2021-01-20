from pprint import pprint

board = [
    [1,2,3, 'uhm',5,6, 'igloo',8,9],
    [4,5,6, 7,8,9, 1,2,3],
    [7,8,9, 1,2,'uhm2', 4,5,'igloo2'],

    ['lol',2,3, 'man',8,9, 'house',5,6],
    [4,5,6, 1,2,3, 7,8,9],
    [7,8,'lol2', 4,5,'man2', 1,2,'house2'],

    ['poop',2,3, 'kite',5,6, 'apple',8,9],
    [4,5,6, 7,8,9, 1,2,3],
    [7,8,'poop2', 1,2,'kite2', 4,5,'apple2']
]

# for m in range(3):
#     for n in range(3):
#         for i in range(m*3, (m+1)*3):
#             for j in range(n*3, (n+1)*3):
#                 print(board[i][j])
#                 pass
# a = [board[i][j] for m in range(3) for n in range(3) for i in range(m*3, (m+1)*3) for j in range(n*3, (n+1)*3)]
def is_valid(board,r,c,test_num):
    board = board
    transposed = [list(i) for i in zip(*board)]
    boxes = [[board[i][j] for i in range(m*3, (m+1)*3) for j in range(n*3, (n+1)*3)] for m in range(3) for n in range(3)]
    box_index = [[j+i*3 for j in range(3)] for i in range(3)]
    return False if test_num in board[r] or test_num in transposed[c] or test_num in boxes[box_index[r//3][c//3]] else True


for r in range(len(board)):
    for c in range(len(board[r])):
        if board[r][c] == 0:
            for test_num in range(1,10):
                board[r][c] = test_num
                #transposed = [list(i) for i in zip(*board)]
                #boxes = [[board[i][j] for i in range(m*3, (m+1)*3) for j in range(n*3, (n+1)*3)] for m in range(3) for n in range(3)]
                if is_valid(board,r,c,test_num):
                    break
                else:

