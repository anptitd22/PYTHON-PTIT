dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
n,m=map(int,input().split())
a=[]
check=[[0 for _ in range(m)]for _ in range(n)]
s=0
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
for i in range(n):
    for j in range(m):
        if a[i][j]==-1:
            for k in range(8):
                ik=i+dx[k]
                jk=j+dy[k]
                if ik<n and ik>=0 and jk<m and jk>=0 and check[ik][jk]==0:
                    s+=a[ik][jk]
                    check[ik][jk]=1
print(s)