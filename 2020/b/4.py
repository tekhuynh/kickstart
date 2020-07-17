import math

def func():
    w, h, l, u, r, d = [int(x) for x in input().split()]
    return binom(w, h, l, u, r, d)

def comb(x, y):
    return math.factorial(x) // math.factorial(y) // math.factorial(x - y)

def binom(w,h,l,u,r,d):
    downrightpaths = 0.5 ** (l + d - 2)
    rightdownpaths = 0.5 **(r + u - 2)

    prob = 0

    #downright
    if d < h:
        n = l + d - 2
        for i in range(l-1):
            prob += comb(n, i) * downrightpaths

    #rightdown
    if r < w:
        n = r + u - 2
        for i in range(u-1):
            prob += comb(n, i) * rightdownpaths 
    
    return prob


def dp(w,h,l,u,r,d):
    grid = [[None] * h for i in range(w)]

    for col in range(l-1, r):
        for row in range (u - 1, d):
            grid[col][row] = 0
    grid[w-1][h-1] = 1

    return dp1(0, 0, w, h, grid)

def dp1(x, y, w, h, grid):
    if x == w or y == h:
        return None
    if grid[x][y] != None:
        return grid[x][y]
    
    down = grid[x][y] = dp1(x, y + 1, w, h, grid)
    right = grid[x][y] = dp1(x + 1, y, w, h, grid)

    if down == None:
        grid[x][y] = right
        return right
    if right == None:
        grid[x][y] = down
        return down

    grid[x][y] = 0.5 * right + 0.5 * down
    return grid[x][y]

t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, func()))