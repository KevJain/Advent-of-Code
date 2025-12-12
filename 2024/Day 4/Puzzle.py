input = open("input.txt").read().split()

def count(grid):
    return sum(row.count("XMAS") + row.count("SAMX") for row in grid)

def get_diagonals(grid):
    m = len(grid)
    n = len(grid[0])
    diagonals = ["" for _ in range(m+n)]
    for rank in range(m + n):
        for i in range(rank+1):
            if i < m and rank - i < n:
                diagonals[rank] += grid[i][rank-i]
    return diagonals

transposed = list(map(lambda t: "".join(t), zip(*map(list, input))))
reversed_input = list(reversed(input))

out = 0
out += count(input)
out += count(transposed)
out += count(get_diagonals(input))
out += count(get_diagonals(reversed_input))

print(out)
cmp = set(["M", "S"])
rows = len(input)
cols = len(input[0])
xmas = 0
for r in range(1, rows-1):
    for c in range(1, cols-1):
        if input[r][c] == 'A':
            if set([input[r-1][c-1], input[r+1][c+1]]) == cmp and set([input[r+1][c-1], input[r-1][c+1]]) == cmp:
                xmas += 1
print(xmas)
