from collections import Counter
# 29379307
input = list(map(int, open("input.txt").read().split()))
l1, l2 = sorted(input[::2]), sorted(input[1::2])
freq = Counter(l2)
print(sum(abs(l1[i] - l2[i]) for i in range(len(l1))))
print(sum(num * freq[num] for num in l1))
