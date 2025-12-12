# Challenge: one liner
import re
print(sum(l // 3 * w // 3 >= sum(v) for l, w, *v in map(lambda s: map(int, re.findall(r'\d+', s)), list(open('input.txt'))[30:])))
