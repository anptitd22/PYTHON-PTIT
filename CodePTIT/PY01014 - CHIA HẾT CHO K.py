a,k,n=map(int,input().split())
ok=1
i=1
while i*k<=n:
    if i*k-a>0:
        ok=0
        for b in range(i*k-a,n-a+1,k):
            print(b,end=" ")
        break
    i+=1
if ok==1:
    print(-1)