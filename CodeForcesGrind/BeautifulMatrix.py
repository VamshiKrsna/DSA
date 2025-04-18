# https://codeforces.com/problemset/problem/263/A

fini = []
x = 0
y = 0
for i in range(5):
    row = list(map(int, input().split()))
    fini.append(row)
    if 1 in row:
        x = i
        y = fini[x].index(1)
print(abs(x - 2) + abs(y - 2))