n,m=map(int,input().split())
a,cnt1,cnt2=[],0,0
if n>m:
    cnt1=n-m
elif n<m:
    cnt2=m-n
for i in range(n):
    b=list(map(int,input().split()))
    if cnt1>0 and i%2==0:
        cnt1-=1
        continue
    if cnt2>0:
        c=[]
        res=cnt2
        for i in range(len(b)):
            if i%2==1 and res>0:
                res-=1
                continue
            c.append(b[i])   
        b=c
    a.append(b)
for x in a:
    for y in x:
        print(y,end=' ')
    print()