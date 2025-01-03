import math
def nto(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return n>1
def check(n):
    res,sum=0,0
    if not nto(n): return False
    while n>0:
        if not nto(n%10):
            return False
        res=res*10+n%10
        sum+=n%10
        n//=10
    return nto(sum) and nto(res)
for t in range(int(input())):
    n=int(input())
    if check(n):
        print("Yes")
    else:
        print("No")