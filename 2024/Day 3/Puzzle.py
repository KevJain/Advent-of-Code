from operator import mul
import re
# 179834255
# 80570939
input = "do()" + open("input.txt").read().replace('\n', "") + "don't()"
p1 = r"mul\(\d{1,3},\d{1,3}\)"
filtered = "".join(re.findall(r"do\(\)(.*?)don't\(\)", input))
print(sum(eval(p) for p in re.findall(p1, input)))
print(sum(eval(p) for p in re.findall(p1, filtered)))
