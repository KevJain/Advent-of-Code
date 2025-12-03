import sys

banks = list(map(lambda x: list(map(int, x)), sys.stdin.read().split()))

s = 0

for bank in banks:
    dp = [0] * 13  # dp[i] = max seq of size i
    for battery in bank:
        for i in range(12, 0, -1):
            cand = 10 * dp[i - 1] + battery
            if dp[i] < cand:
                dp[i] = cand
    s += dp[12]
print(s)
