import random
import time
import os
clear = lambda: os.system('cls')
clear()

class Grid:
    def __init__(self):
        


def create_grid(item): return [[item for _ in range(4)] for _ in range(4)]
def flatten(grid): return sum(grid,[])
def spawn_tile(grid):
    if 0 not in flatten(grid): return grid, True
    while True:
        r = random.randint(0,3)
        c = random.randint(0,3)
        if grid[r][c] == 0:
            grid[r][c] = 2
            return grid, False

def gprint(grid):
    grid = [[str(grid[r][c]) if grid[r][c] != 0 else "☐" for c in range(4)] for r in range(4)]
    for i in range(4):
        print(f"{' '.join(grid[i])}")
    print()

def main(grid, direction):

    def left(grid):
        grid_merged = create_grid(False)
        for r in range(4):
            for c in range(1,4):
                for n in range(c):
                    if grid[r][c-n] != 0:
                        if grid[r][c-1-n] == 0:
                            grid[r][c-1-n] = grid[r][c-n]
                            grid[r][c-n] = 0
                        else:
                            if grid[r][c-1-n] == grid[r][c-n] and not grid_merged[r][c-n] and not grid_merged[r][c-1-n]:
                                grid[r][c-1-n] += grid[r][c-n]
                                grid[r][c-n] = 0
                                grid_merged[r][c-1-n] = True
        return grid

    def hflip(grid): return [r[::-1] for r in grid]
    def tpose(grid): return [list(tup) for tup in zip(*grid)]

    def right(grid): return hflip(left(hflip(grid)))
    def up(grid): return tpose(left(tpose(grid)))
    def down(grid): return tpose(hflip(left(hflip(tpose(grid)))))

    if direction == "L": grid = left(grid)
    elif direction == "'": grid = right(grid)
    elif direction == "P": grid = up(grid)
    elif direction == ";": grid = down(grid)

    grid, gameover = spawn_tile(grid)
    if gameover:
        input(f"\nGame Over!\nHighest: {max(flatten(grid))}\nHighscore: {sum(flatten(grid))}")
        quit()

    return grid

def init_grid(grid):
    for _ in range(2): grid, _ = spawn_tile(grid)
    return grid

grid = create_grid(0)
grid = init_grid(grid) 
gprint(grid)

while True:
    try:
        direction = input(">> ").upper()
        if direction == "X": quit()
        grid = main(grid, direction)
        clear()
        gprint(grid)
    except Exception as e:
        print(e)