def check(a, u, v, e, n):
    q, ok = [u], [0]*(n+1)
    ok[u] = 1
    while len(q)>0:
        x = q.pop()
        if x==v: return False
        for i in range(1,n+1):
            if a[x][i]==1 and ok[i]==0 and i!=e:
                q.append(i)
                ok[i]=1
    return True
for t in range(int(input())):
    n, m, u, v = map(int, input().split())
    a=[[0 for _ in range(n+1)]for _ in range(n+1)]
    for i in range(m):
        x, y = map(int, input().split())
        a[x][y]=1
    cnt = 0  
    for i in range(n+1):
        if i!=u and i!=v:
            if check(a, u, v, i, n): 
                cnt+=1
    print(cnt)