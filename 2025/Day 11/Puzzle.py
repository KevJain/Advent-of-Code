import sys
from collections import defaultdict

raw_input = sys.stdin.readlines()

def dfs(cur): # Part 1 DFS
    if cur == 'out':
        return 1
    num_ways = 0
    for next_node in graph[cur]:
        num_ways += dfs(next_node)
    return num_ways

def topo_sort(cur):
    if cur in seen:
        return
    seen.add(cur)
    for neighbour in graph[cur]:
        topo_sort(neighbour)
    tsort.append(cur)

graph = defaultdict(list)
for line in raw_input:
    nodes = line.split()
    node = nodes[0][:-1]
    for neighbour in nodes[1:]:
        graph[node].append(neighbour)

tsort = []
seen = set()
topo_sort('svr')
tsort.reverse()
#print(tsort) # fft appears before dac in topological sort
dp = {node : [0,0,0] for node in tsort}
dp['svr'][0] = 1
for node in tsort:
    for neighbour in graph[node]:
        if neighbour == 'fft':
            dp[neighbour][1] += dp[node][0]
        elif neighbour == 'dac':
            dp[neighbour][2] += dp[node][1]
        else:
            for i in range(3):
                dp[neighbour][i] += dp[node][i]
#print(dp)
print(dp['out'][2])
#dfs2('svr')
