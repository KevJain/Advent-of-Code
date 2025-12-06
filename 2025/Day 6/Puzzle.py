import sys

rows = []
while True:
    line = sys.stdin.readline()
    if not line:
        break
    rows.append(line[:-1])
row_width = len(rows[-1])
for row in rows:
    print(row)

terms = []
for col in range(row_width):
    cur_term = ""
    for row in range(len(rows) - 1):
        cur_term += rows[row][col]
    stripped = cur_term.strip()
    terms.append(int(stripped) if stripped else 0)

cur_term = 0
op = "+"
out = 0
for col in range(row_width):
    if terms[col] == 0:
        out += cur_term
        print(cur_term)
        continue
    if rows[-1][col] != " ":
        op = rows[-1][col]
        cur_term = terms[col]
    else:
        cur_term = eval(str(cur_term) + op + str(terms[col]))

out += cur_term
print(out)
