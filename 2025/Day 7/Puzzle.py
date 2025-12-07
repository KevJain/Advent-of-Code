import sys


def to_num(c):
    if c == ".":
        return 0
    elif c == "^":
        return -1
    return 1


rows = list(map(list, sys.stdin.read().split()))
rows = [[to_num(e) for e in row] for row in rows]
size = len(rows[0])


for row in range(1, len(rows)):
    for col in range(size):
        if rows[row - 1][col] > 0:
            if rows[row][col] == -1:
                rows[row][col - 1] += rows[row - 1][col]
                rows[row][col + 1] += rows[row - 1][col]
            else:
                rows[row][col] += rows[row - 1][col]

for row in rows:
    print(row)
print(sum(rows[-1]))
