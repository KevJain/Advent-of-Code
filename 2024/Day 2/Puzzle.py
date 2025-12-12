# 269, 337
reports = [[*map(int, line.split())] for line in open("input.txt")]
def safe(l) -> bool:
    diffs = [l[i+1] - l[i] for i in range(len(l) - 1)]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)

def safe_damp(l) -> bool:
    return safe(l) or any(safe(l[:i] + l[i+1:]) for i in range(len(l)))

print(sum(safe(report) for report in reports))
print(sum(safe_damp(report) for report in reports))
