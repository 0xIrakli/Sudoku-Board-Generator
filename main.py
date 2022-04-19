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
    posibilities = []
    for y in range(9):
        posibilities.append([])
        for x in range(9):
            posibilities[y].append(list(range(1, 10)))
    return posibilities
   
def blank_quadposibilities():
    quadpos = []
    for y in range(3):
        quadpos.append([])
        for x in range(3):
            quadpos[y].append(list(range(1, 10)))
    return quadpos
    
def fill(g):
    posibilities = blank_posibilities()
    quadpos = blank_quadposibilities()
    
    for y in range(9):
        for x in range(9):
            qX = x//3
            qY = y//3
            choice = rand.choice(list(set(posibilities[y][x]) & set(quadpos[qY][qX])))
            g[y][x] = choice
            
            #remove number from this row, this column and this *quadrant*. 
            if choice in quadpos[qY][qX]:
                quadpos[qY][qX].remove(choice)
            
            for row in posibilities:
                if choice in row[x]:
                    row[x].remove(choice)
                    
            for col in posibilities[y]:
                if choice in col:
                    col.remove(choice)
fill0s(grid)
while True:
    try:
        fill(grid)
        prnt(grid)
        sums = []
        for y in range(len(grid)):
            sums.append(0)
            for x in range(len(grid[y])):
                sums[y] += grid[x][y]
        #print(sums)
        #print(list(map(sum, grid)))
        break
    except:
        pass
