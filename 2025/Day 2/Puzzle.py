import sys

divisors = {1: []}
for i in range(2, 11):
    divisors[i] = []
    for j in range(1, i):
        if i % j == 0:
            divisors[i].append(j)


def is_double(num):
    str_num = str(num)
    l = len(str_num)
    return l % 2 == 0 and str_num[: l // 2] == str_num[l // 2 :]


def invalid(num):
    str_num = str(num)
    l = len(str_num)
    for d in divisors[l]:
        ret = True
        for base in range(1, l // d):
            if str_num[:d] != str_num[base * d : (base + 1) * d]:
                ret = False
        if ret:
            return True
    return False


ranges = list(map(lambda s: list(map(int, s.split("-"))), sys.stdin.read().split(",")))

s = 0
for lower, upper in ranges:
    for num in range(lower, upper + 1):
        if invalid(num):
            s += num

print(s)
