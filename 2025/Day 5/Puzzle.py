import bisect
import sys

full_in = sys.stdin.read().split()

intervals = []
queries = []

for s in full_in:
    if "-" in s:
        intervals.append(list(map(int, s.split("-"))))
    else:
        queries.append(int(s))

intervals.sort()
merged = []
cur_start = intervals[0][0]
cur_end = intervals[0][1]

for start, end in intervals[1:]:
    if start <= cur_end + 1:
        cur_end = max(cur_end, end)
    else:
        merged.append([cur_start, cur_end])
        cur_start = start
        cur_end = end

merged.append([cur_start, cur_end])
fresh = 0

for q in queries:
    loc = bisect.bisect_right(merged, q, key=lambda m: m[0]) - 1
    if loc >= 0 and merged[loc][1] >= q:
        fresh += 1

total_fresh = 0
for start, end in merged:
    total_fresh += end - start + 1

print(fresh)
print(total_fresh)
