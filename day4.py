with open('day4.txt') as f: s = f.readlines()

def is_xmas(grid, row, col, dir):
    n, m = len(grid), len(grid[0]) - 1
    letters = ['M', 'A', 'S']
    for i in range(3):
        row += dir[0]
        col += dir[1]
        if row < 0 or row >= n or col < 0 or col >= m: 
            return False
        elif grid[row][col] != letters[i]:
            return False
    return True

def is_max(grid, row, col, cross):
    c1 = grid[row + cross[0][0]][col + cross[0][1]]
    c2 = grid[row + cross[1][0]][col + cross[1][1]]

    if (c1 == 'M' and c2 == 'S') or (c1 == 'S' and c2 == 'M'):
        return True
    else:
        return False

def day4_part1(grid):
    res = 0
    dirs = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1, 1)]
    n, m = len(grid), len(grid[0]) - 1 # need -1 for the /n char

    for row in range(n):
        for col in range(m):
            if grid[row][col] == 'X':
                for dir in dirs:
                    if is_xmas(grid, row, col, dir):
                        res += 1
    return res

def day4_part2(grid):
    res = 0
    corners = [[(1,1), (-1,-1)], [(-1,1), (1,-1)]]
    n, m = len(grid), len(grid[0]) - 1 # need -1 for the /n char
    for row in range(1, n - 1):
        for col in range(1, m - 1):
            if grid[row][col] == 'A':
                if is_max(grid, row, col, corners[0]) and is_max(grid, row, col, corners[1]):
                    res += 1
    return res



print(day4_part1(s))
print(day4_part2(s))

