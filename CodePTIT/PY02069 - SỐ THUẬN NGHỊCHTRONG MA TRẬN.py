from math import sqrt
def nt(x):
    if len(x)==1:
        return False
    y=x[::-1]
    return x==y
a, ans, check, max = [], [], True, 11
n, m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if nt(str(a[i][j])):
            check = False
            if a[i][j] == max: ans.append((i, j))
            elif a[i][j] > max:
                ans = [(i, j)]
                max = a[i][j]
if check: print('NOT FOUND')
else:
    print(max)
    for i in ans:
        print(f'Vi tri [{i[0]}][{i[1]}]')