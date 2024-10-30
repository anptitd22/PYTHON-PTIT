n,k=map(int,input().split())
k=min(k,n)
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[[0,0] for _ in range(n)]
for i in range(n):
    c[i][0]=a[i]-b[i]
    c[i][1]=i
c.sort(key=lambda x:x[0])
sum=0
for i in range(k):
    sum+=a[c[i][1]]
for i in range(k,n):
    if c[i][0]>=0:
        sum+=b[c[i][1]]
    else:
        sum+=a[c[i][1]]
print(sum)