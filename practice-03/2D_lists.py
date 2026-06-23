grid = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    for j in range(4):
        if i == j:
            grid[i][j] = 1

for row in grid:
    print(" ".join(str(value)for value in row))