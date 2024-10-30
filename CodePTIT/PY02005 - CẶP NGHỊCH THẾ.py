import math
def merge(a,l,m,r):
    x=a[l:m+1]
    y=a[m+1:r+1]
    i,j,cnt=0,0,0
    while i<len(x) and j<len(y):
        if x[i]<=y[j]:
            a[l]=x[i]
            l+=1
            i+=1
        else:
            cnt+=len(x)-i
            a[l]=y[j]
            l+=1
            j+=1
    while i<len(x):
        a[l]=x[i]
        l+=1
        i+=1
    while j<len(y):
        a[l]=y[j]
        l+=1
        j+=1
    return cnt
def mergesort(a,l,r):
    dem=0
    if l<r:
        m=(l+r)//2
        dem+=mergesort(a,l,m)
        dem+=mergesort(a,m+1,r)
        dem+=merge(a,l,m,r)
    return dem
n=int(input())
a=list(map(int,input().split()))
print(mergesort(a,0,n-1))