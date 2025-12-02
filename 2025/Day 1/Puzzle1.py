import sys

moves = list(sys.stdin.read().split())

loc = 50
count = 0
for move in moves:
    dir = move[0]
    clicks = int(move[1:])
    was_zero = loc == 0
    if dir == "R":
        loc += clicks
    else:
        loc -= clicks
    print(loc)
    if loc <= 0:
        count += 1 + (-loc) // 100 - (1 if was_zero else 0)
        loc %= 100
    elif loc >= 100:
        count += loc // 100
        loc %= 100

print(count)
