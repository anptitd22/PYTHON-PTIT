import math
def lower_bow(n,l,r,x):
    if l>r:
        return l
    m=(l+r)//2
    if n[m]<x:
        return lower_bow(n,m+1,r,x)
    elif n[m]==x:
        return m
    else:
        return lower_bow(n,l,m-1,x)
pri=[True]*(10**6+1)
d=[]
pri[0]=pri[1]=False
for i in range(2,math.isqrt(10**6)):
    if pri[i]:
        d.append(i)
        for j in range(i*i,10**6+1,i):
            pri[j]=False
for i in range(math.isqrt(10**6)+1,10**6):
    if pri[i]:
        d.append(i)
n=int(input())
a=list(map(int,input().split()))
minn=0
for i in range(len(a)):
    if not pri[a[i]]:
        x=lower_bow(d,0,len(d)-1,a[i])
        if x>0 and x<len(d):
            res=min(abs(a[i]-d[x]),abs(a[i]-d[x-1]))
            minn=max(minn,res)
        elif x==len(d):
            re.append(a[i]-d[x-1])
            minn=max(minn,a[i]-d[x-1])
        else:
            re.append(d[x]-a[i])
            minn=max(minn,d[x]-a[i])
print(minn)