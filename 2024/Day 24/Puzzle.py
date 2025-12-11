from collections import defaultdict
from collections import deque
I, G = open('input.txt').read().strip().split('\n\n')
values = {w[:-1] : int(v) for w, v in map(lambda s: s.split(), I.split('\n'))}
children = defaultdict(list)
calc = {}
op_map = {"AND" : "&", "OR" : "|", "XOR" : "^"}
queue = deque()
for gate in G.split('\n'):
    in1, op, in2, _, out = gate.split()
    children[in1].append(out)
    children[in2].append(out)
    calc[out] = [in1, in2, op]
    if in1 in values and in2 in values:
        queue.append(out)

while queue:
    out = queue.popleft()
    in1, in2, op = calc[out]
    values[out] = eval(f"values['{in1}'] " + op_map[op] + f" values['{in2}']")
    for child in children[out]:
        if calc[child][0] in values and calc[child][1] in values:
            queue.append(child)

total = 0

for wire, val in sorted(values.items()):
    if wire[0] != 'z':
        continue
    total += val << (int(wire[1:]))

print(total)
