from collections import defaultdict
from functools import cmp_to_key
g, u = open("input.txt").read().split('\n\n')

graph = defaultdict(set)
for cond in g.split('\n'):
    pre, post = cond.split("|")
    graph[pre].add(post)

updates = [line.split(',') for line in u.split()]

out = 0
incorrect = []
for update in updates:
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[i] in graph[update[j]]:
                incorrect.append(update)
                break
        else:
            continue
        break
    else:
        out += int(update[len(update)//2])

def cmp(x, y):
    return -1 if y in graph[x] else 1

out2 = 0
for update in incorrect:
    update.sort(key = cmp_to_key(cmp))
    out2 += int(update[len(update)//2])
print(out)
print(out2)
