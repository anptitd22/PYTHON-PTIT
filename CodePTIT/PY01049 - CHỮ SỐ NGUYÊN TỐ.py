import math
def nto(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return n>1
def check(n):
    if not nto(len(n)): return False
    b=[x for x in a if nto(x)]
    return len(b)>len(a)/2
t=int(input())
for test in range(t):
    a=list(map(int,input()))
    if check(a):
        print("YES")
    else:
        print("NO")