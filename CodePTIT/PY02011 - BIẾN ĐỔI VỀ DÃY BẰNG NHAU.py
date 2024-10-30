n=int(input())
a=list(map(int,input().split()))
minn,res=1e8+1,0
for i in range(len(a)):
    tong=0
    for j in range(len(a)):
        tong+=abs(a[j]-a[i])
    if tong<minn:
        minn=tong
        res=a[i]
print(minn,res)