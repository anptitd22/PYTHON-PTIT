n=int(input())
cnt=[0]*(n+1)
for i in range(n-1):
    x,y=map(int,input().split())
    cnt[x]+=1
    cnt[y]+=1
ans=0
for i in range(1,n+1):
    if cnt[i]==1:
        ans+=1
if ans!=n-1:
    print("No")
else:
    print('Yes')