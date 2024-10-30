import math
def ngto(n):
    if n<2: return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0: return False
    return True
def tong(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return ngto(sum)
t=int(input())
for test in range(t):
    a,b=map(int,input().split())
    if tong(math.gcd(a,b)):
        print("YES")
    else:
        print("NO")