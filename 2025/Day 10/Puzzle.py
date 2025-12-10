import sys

from z3 import *

raw_input = sys.stdin.readlines()
targets = []  # target for each machine
buttons = []  # buttons for each machine
joltage = []


def list_to_mask(l):
    out = 0
    for b in l[1:-1].split(","):
        out += 1 << int(b)
    return out


def str_mask_to_mask(smask):
    out = 0
    for i in range(len(smask)):
        if smask[i] == "#":
            out += 1 << i
    return out


def bitcount(x):
    out = 0
    while x > 0:
        if x & 1:
            out += 1
        x >>= 1
    return out


def solveLP(A, b, c) -> int: # Use Z3 to solve LPs of the form minimize c * x, with Ax = b and x >= 0, note b and c are row vectors
    opt = Optimize()
    x = [Int(f"x_{i}") for i in range(len(c))]

    for i in range(len(A)):
        lhs = sum(A[i][j] * x[j] for j in range(len(x)))
        opt.add(lhs == b[i])

    for j in range(len(c)):
        opt.add(x[j] >= 0)

    obj = sum(c[j] * x[j] for j in range(len(c)))
    opt.minimize(obj)
    opt.check()
    model = opt.model()
    return model.evaluate(obj).as_long()

presses = 0
for line in raw_input:
    line = line.split()

    """
    target = str_mask_to_mask(line[0][1:-1])
    button_list = [list_to_mask(l) for l in line[1:-1]]
    min_presses = len(button_list)
    for mask in range(1 << len(button_list)):
        state = 0
        for b in range(len(button_list)):
            if mask >> b & 1:
                state ^= button_list[b]
        if state == target:
            min_presses = min(min_presses, bitcount(mask))
        presses += min_presses
    """
    # print(line, min_presses)
    b_lists = [[int(b) for b in l[1:-1].split(",")] for l in line[1:-1]]
    joltages = [int(j) for j in line[-1][1:-1].split(",")]
    A = [[0] * len(b_lists) for _ in range(len(joltages))]
    for i, buttons in enumerate(b_lists):
        for button in buttons:
            A[button][i] = 1
    c = [1] * len(b_lists)
    presses += solveLP(A, joltages, c)

print(presses)
