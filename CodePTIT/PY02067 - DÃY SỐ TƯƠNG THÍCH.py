n=int(input())
a=list(map(int,input().split()))
b=[[0 for _ in range(2001)]for _ in range(2001)]
cnt=0
for i in range(n):
    b[0][a[i]]+=1
    b[a[i]][0]+=1
    for j in range(2,a[i]//2+2):
        if a[i]//j != a[i]//(j-1):
            b[0][a[i]//j]+=1
            b[a[i]//j][0]+=j
minn=1e5
for i in range(1002):
    if b[0][i]==n:
        minn=min(minn,b[i][0])
print(minn)       