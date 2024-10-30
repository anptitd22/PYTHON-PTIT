import math
h=[]
def binary_search(a,l,r,x):
    if l>r: return 'Not in sequence'
    m=(l+r)//2
    if a[m]==x: return m+1
    elif a[m]<x: return binary_search(a,m+1,r,x)
    else: return binary_search(a,l,m-1,x)
i=1
while i<=10**18:
    j=1
    while j<=10**18:
        k=1
        while k<=10**18:
            h.append(i*j*k)
            k*=5
        j*=3
    i*=2   
h.sort()
for t in range(int(input())):
    n=int(input())
    print(binary_search(h,0,len(h),n))