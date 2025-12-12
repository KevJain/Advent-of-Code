import time
# CPython: 30.594339s
# PyPy3: 0.939207s
grid = list(map(list, open("input.txt").read().split()))
dirs = [(-1,0),(0,1),(1,0),(0,-1)]
m, n = len(grid), len(grid[0])

start_time = time.perf_counter()
start_r, start_c = -1, -1

for row in range(m):
    for col in range(n):
        if grid[row][col] == '^':
            start_r, start_c = row, col

places = 0
for row in range(m):
    for col in range(n):
        if grid[row][col] != '.':
            continue
        visited = [[0 for _ in range(n)] for _ in range(m)] # visited[r][c][d] = visited r,c with direction d
        grid[row][col] = '#'
        loop = False
        r, c = start_r, start_c
        dir = 0
        while 0 <= r < m and 0 <= c < n:
            if visited[r][c] >> dir & 1:
                loop = True
                break
            visited[r][c] += 1 << dir
            nr, nc = r + dirs[dir][0], c + dirs[dir][1]
            while 0<=nr<m and 0<=nc<n and grid[nr][nc] == '#':
                dir = (dir + 1) % 4
                visited[r][c] += 1 << dir
                nr, nc = r + dirs[dir][0], c + dirs[dir][1]
            r, c = nr, nc
        if loop:
            places += 1
            """ Pretty print looped grid
            for vrow in range(m):
                for vcol in range(n):
                    cell = visited[vrow][vcol]
                    if cell & 5 and cell & 10:
                        print('+', end="")
                    elif cell & 5:
                        print('|', end="")
                    elif cell & 10:
                        print('–', end="")
                    else:
                        print(grid[vrow][vcol], end="")
                print()
            print()
            """
        grid[row][col] = '.'
#out = sum(sum(any(cell) for cell in row) for row in visited)

end_time = time.perf_counter()
elapsed = end_time - start_time
print(f'Completed in {elapsed:.6f}s')
print(places)
