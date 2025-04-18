# https://codeforces.com/problemset/problem/282/A
n = int(input())
temp = 0
for i in range(n):
    inp = input()
    if inp in ["X++","++X"]:
        temp += 1
    else:
        temp -= 1
print(temp)