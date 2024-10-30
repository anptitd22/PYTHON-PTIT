import math
# prime=[True]*(10**6+1)
# def pre():
#     prime[0]=prime[1]=False
#     for i in range(2,math.isqrt(10**6)):
#         if prime[i]:
#             for j in range(i*i,10**6+1,i):
#                 prime[j]=False
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
# pre()
n=int(input())
a=list(map(int,input().split()))
# a=[x for x in a if prime[x]]
a.sort()
quay(a,0,n,[],check)
# print(a)