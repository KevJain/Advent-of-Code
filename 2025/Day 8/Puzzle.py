import heapq
import sys

raw_input = sys.stdin.read().split()
nodes = [list(map(int, s.split(","))) for s in raw_input]

root = [i for i in range(len(nodes))]


def get_root(x):
    if root[x] != x:
        root[x] = get_root(root[x])
    return root[x]


def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2


pq = []

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        d = dist(nodes[i], nodes[j])
        heapq.heappush(pq, (d, i, j))

""" Part 1:
csize = [1 for i in range(len(nodes))]
for _ in range(1000):
    _, i, j = heapq.heappop(pq)
    root_i = get_root(i)
    root_j = get_root(j)
    if root_i != root_j:
        if csize[root_i] > csize[root_j]:
            csize[root_i] += csize[root_j]
            root[root_j] = root[root_i]
        else:
            csize[root_j] += csize[root_i]
            root[root_i] = root[root_j]

csize.sort(reverse=True)
print(csize[0] * csize[1] * csize[2])

"""

components = len(nodes)
while pq:
    _, i, j = heapq.heappop(pq)
    root_i = get_root(i)
    root_j = get_root(j)
    if root_i != root_j:
        if components == 2:
            print(f"Found last two nodes: {i}, {j}")
            print(nodes[i][0] * nodes[j][0])
            break
        components -= 1
        root[root_j] = root_i
