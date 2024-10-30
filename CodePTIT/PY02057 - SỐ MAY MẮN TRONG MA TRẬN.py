from math import sqrt
a, ans, check, maxx,minn = [], [], True, -1e9,1e5
n, m = map(int, input().split())
for i in range(n):
    b=list(map(int, input().split()))
    maxx=max(maxx,max(b))
    minn=min(minn,min(b))
    a.append(b)
for i in range(n):
    for j in range(m):
        if a[i][j]==maxx-minn:
            check = False
            ans.append((i, j))
if check: print('NOT FOUND')
else:
    print(maxx-minn)
    for i in ans:
        print(f'Vi tri [{i[0]}][{i[1]}]')