import math
pre=[True]*(10**6+1)
def prime():
    pre[0]=pre[1]=False
    for i in range(2,math.isqrt(10**6)):
        if pre[i]:
            for j in range(i*i,10**6+1,i):
                pre[j]=False      
prime()         
n=int(input())
a=list(map(int,input().split()))
a=[x for x in a if pre[x]]
d=dict({})
for x in a:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
for x in a:
    if x in d:
        print(x,d[x])
        del d[x]