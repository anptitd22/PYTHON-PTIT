n=int(input())
cnt=[0]*30001
a=list(map(int,input().split()))
minn,maxx,ok=30001,0,0
for i in a:
    minn=min(minn,i)
    maxx=max(maxx,i)
    cnt[i]=1
for i in range(minn,maxx+1):
    if cnt[i]!=1:
        print(i)
        ok=1
        break
if ok==0:
    print(maxx+1)