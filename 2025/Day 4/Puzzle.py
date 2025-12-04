"""
Finished in 0.044711 seconds, 10x faster than slower
"""

import sys
import time
from collections import deque

grid = list(map(list, sys.stdin.read().split()))
start_time = time.perf_counter()

count = 0
m = len(grid)
n = len(grid[0])

q = deque()  # (row, col) to be removed
neighbours = [[0] * n for _ in range(m)]
adj_list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(m):
    for j in range(n):
        if grid[i][j] == "@":
            for di, dj in adj_list:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "@":
                    neighbours[i][j] += 1
            if neighbours[i][j] < 4:
                q.append((i, j))

while len(q) > 0:
    row, col = q.popleft()
    if (grid[row][col]) != "@":
        continue
    grid[row][col] = "x"
    count += 1
    for dr, dc in adj_list:
        nr, nc = row + dr, col + dc
        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "@":
            neighbours[nr][nc] -= 1
            if neighbours[nr][nc] < 4:
                q.append((nr, nc))

end_time = time.perf_counter()
elapsed = end_time - start_time

print(count)
print(f"Finished in {elapsed:.6f} seconds")
