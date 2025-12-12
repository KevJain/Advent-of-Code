from collections import defaultdict

grid = defaultdict(str) | {(i,j): c for i, row in enumerate(open("input.txt")) for j, c in enumerate(row)}
dirs = (-1, 0, 1)
cells = list(grid.keys())
print(sum("XMAS" == "".join(grid[(r+dr*i,c+dc*i)] for i in range(4)) for (r,c) in cells for dr in dirs for dc in dirs))
targets = ("SAM", "MAS")
print(sum("".join(grid[(r+d,c+d)] for d in dirs) in targets and
"".join(grid[(r-d, c+d)] for d in dirs) in targets for (r,c) in cells))
