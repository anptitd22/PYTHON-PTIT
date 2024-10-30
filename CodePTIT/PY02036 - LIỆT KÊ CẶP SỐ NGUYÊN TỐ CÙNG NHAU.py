import math
check=[True]*101
def quay(a,i,n,r,check):
    if len(r)==2:
        if math.gcd(r[0],r[1])==1:
            for k in range(len(r)):
                print(r[k],end=' ')
            print()
        return
    for j in range(i,n):
        if check[j]:
            check[j]=False
            r.append(a[j])
            if j<n:
                quay(a,j+1,n,r,check)
            r.pop()
            check[j]=True
n=int(input())
a=list(map(int,input().split()))
a.sort()
quay(a,0,n,[],check)