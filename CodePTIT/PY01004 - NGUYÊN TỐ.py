from math import *
def prime(n):
    if n<2: return False
    for i in range(2,isqrt(n)+1):
        if(n%i==0): return False
    return True
t=int(input())
for i in range(t):
    n=int(input())
    k=0
    for j in range(1,n):
        if gcd(n,j)==1:
            k+=1
    if prime(k):
        print("YES")
    else:
        print("NO")