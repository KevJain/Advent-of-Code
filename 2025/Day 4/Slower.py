"""
Finished in 0.535972 seconds
"""

import sys
import time

grid = list(map(list, sys.stdin.read().split()))
start_time = time.perf_counter()

count = 0
m = len(grid)
n = len(grid[0])

adj_list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while True:
    removed = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                neighbours = 0
                for di, dj in adj_list:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "@":
                        neighbours += 1
                if neighbours < 4:
                    removed.append((i, j))
    if len(removed) == 0:
        break
    for row, col in removed:
        grid[row][col] = "."
    count += len(removed)

end_time = time.perf_counter()
elapsed = end_time - start_time

print(count)
print(f"Finished in {elapsed:.6f} seconds")
