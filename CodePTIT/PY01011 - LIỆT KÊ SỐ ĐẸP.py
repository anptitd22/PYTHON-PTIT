import math
def so(n):
    return n in '02468'
def check1(n):
    if len(n)%2==1: return False
    l=0
    r=len(n)-1
    m=(l+r)//2
    while l<r:
        if n[l]!=n[r] or not so(n[l]) or not so(n[r]):
            return False
        l+=1
        r-=1
    return so(n[m])
t=int(input())
for test in range(t):
    n=int(input())
    for i in range(0,n,2):
        if check1(str(i)):
            print(i,end=' ')
    print()