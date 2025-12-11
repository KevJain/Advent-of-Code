import sys
import time
from collections import defaultdict
from functools import cache

raw_input = sys.stdin.readlines()

graph = defaultdict(list)
for line in raw_input:
    nodes = line.split()
    node = nodes[0][:-1]
    for neighbour in nodes[1:]:
        graph[node].append(neighbour)

def dfs(cur): # Part 1 DFS
    if cur == 'out':
        return 1
    num_ways = 0
    for next_node in graph[cur]:
        num_ways += dfs(next_node)
    return num_ways

def topological_dp():
    def topo_sort(cur):
        if cur in seen:
            return
        seen.add(cur)
        for neighbour in graph[cur]:
            topo_sort(neighbour)
        tsort.append(cur)

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

    return dp['out'][2]

def multiplicative_dfs():
    @cache
    def dfs1(cur, target):
        return cur == target or sum(dfs1(neighbour, target) for neighbour in graph[cur])

    return dfs1('svr', 'fft') * dfs1('fft', 'dac') * dfs1('dac', 'out')

start_time = time.perf_counter()
ans = topological_dp()
end_time = time.perf_counter()
elapsed = end_time - start_time
print(ans)
print(f"Finished topological sort + dp in {elapsed:.6f} seconds")

start_time = time.perf_counter()
ans = multiplicative_dfs()
end_time = time.perf_counter()
print(ans)
elapsed = end_time - start_time
print(f"Finished multiplicative dfs in {elapsed:.6f} seconds")
