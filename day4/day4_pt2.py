from day4_pt1 import neighbors8

with open("input.txt", "r") as file:
    input = file.read() 

input = [list(i) for i in input.split("\n")]

def remove_accessible_positions(grid):
    m = len(grid)
    if m == 0:
        return 0
    n = len(grid[0])
    accessible = []
    for x in range(m):
        for y in range(n):
            if grid[x][y] != "@":
                continue
            c = 0
            for nx, ny in neighbors8(x, y, m, n):
                if grid[nx][ny] == "@":
                    c += 1
                    if c > 3:
                        break
            if c <= 3:
                accessible.append((x,y))
    
    for x, y in accessible:
        input[x][y] = "."
    
    return accessible

removed = 0
while True:
    acc = remove_accessible_positions(input)
    if not acc:
        break
    removed += len(acc)
    for x, y in acc:
        input[x][y] = "."   # remove the accessible '@'

print(removed)