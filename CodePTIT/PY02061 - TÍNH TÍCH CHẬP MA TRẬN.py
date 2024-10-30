for t in range(int(input())):
    n,m=map(int,input().split())
    x,h=[],[]
    for i in range(n):
        b=list(map(int,input().split()))
        x.append(b)
    for i in range(3):
        b=list(map(int,input().split()))
        h.append(b)
    y=[[0 for _ in range(m-3+1)] for _ in range(n-3+1)]
    tong=0
    for i in range(n-3+1):
        for j in range(m-3+1):
            for k1 in range(3):
                for k2 in range(3):
                    y[i][j]+=h[k1][k2]*x[i+k1][j+k2]
            tong+=y[i][j]
    print(tong)