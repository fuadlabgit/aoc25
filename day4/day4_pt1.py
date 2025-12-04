
with open("input.txt", "r") as file:
    input = file.read() 

input = [list(i) for i in input.split("\n")]
# print(input[1][0])

def neighbors8(x, y, m, n):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                yield nx, ny

def count_accessible_at_positions(grid):
    m = len(grid)
    if m == 0:
        return 0
    n = len(grid[0])
    accessible = 0
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
                accessible += 1
    return accessible

print(count_accessible_at_positions(input))
