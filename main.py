import random as rand

grid = []

def fill0s(g):
    for i in range(9):
        g.append([])
        for j in range(9):
            g[i].append(0)

def prnt(g):
    for y in range(len(g)):
        if y%3 == 0:
            print('+'+'-'*29+'+')
        for x in range(len(g[y])):
            if x%3 == 0:
                print('|', end='')
            print(f' {g[y][x]} ', end='')
        print('|')
    print('+'+'-'*29+'+')

def blank_posibilities():
    row_posibilities = []
    col_posibilities = []
    for y in range(9):
        row_posibilities.append(list(range(1, 10)))
        col_posibilities.append(list(range(1, 10)))
    return row_posibilities, col_posibilities
   
def blank_quadposibilities():
    quadpos = []
    for y in range(3):
        quadpos.append([])
        for x in range(3):
            quadpos[y].append(list(range(1, 10)))
    return quadpos
    
def fill(g):
    row_posibilities, col_posibilities = blank_posibilities()
    quadpos = blank_quadposibilities()
    
    for y in range(9):
        for x in range(9):
            qX = x//3
            qY = y//3
            try:
                choice = rand.choice(list(set(row_posibilities[y]) & set(col_posibilities[x]) & set(quadpos[qY][qX])))
            except:
                return False

            g[y][x] = choice
            
            #remove number from this row-s, this column-s and this *quadrant*-s choices. 
            if choice in quadpos[qY][qX]:
                quadpos[qY][qX].remove(choice)
            
            if choice in row_posibilities[y]:
                row_posibilities[y].remove(choice)
                    
            if choice in col_posibilities[x]:
                col_posibilities[x].remove(choice)
    return row_posibilities

def solve(board):
    for y, row in enumerate(board):
        for x, col in enumerate(board[y]):
            if col == 0:
                col = []
                for c in range(9): col.append(board[c][x])
                rowposs = row.copy()
                colposs = col.copy()
                

fill0s(grid)
while True:
    pos = fill(grid)
    if pos != False:
        prnt(grid)
        #debug stuff:
        #sums = []
        #for y in range(len(grid)):
        #    sums.append(0)
        #    for x in range(len(grid[y])):
        #        sums[y] += grid[x][y]
        #print(sums)
        #print(list(map(sum, grid)))
        break
