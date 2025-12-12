from functools import cmp_to_key

def cmp(x, y):
    return -(x + "|" + y in rule_set)

rules, pages_list = open("input.txt").read().split("\n\n")
rule_set = set(rules.split())
pages = [(p.split(","), sorted(p.split(","), key = cmp_to_key(cmp))) for p in pages_list.split()]
print(sum(int(p[len(p)//2]) for p, sp in pages if p == sp))
print(sum(int(sp[len(sp)//2]) for p, sp in pages if p != sp))
