import math
def upper_bow(n,l,r,x):
    if l>r:
        return l
    m=(l+r)//2
    if n[m]<=x:
        return upper_bow(n,m+1,r,x)
    else:
        return upper_bow(n,l,m-1,x)
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
cnt=1
for i in range(1,n):
    if a[i]-a[i-1]>k:
        cnt+=1
print(cnt)