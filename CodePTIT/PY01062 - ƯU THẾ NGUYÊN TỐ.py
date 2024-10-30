import math
def nto(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return n>1
def check(n):
    if not nto(len(n)):
        return False
    b=[x for x in n if nto(x)]
    return len(b)>len(n)/2
t=int(input())
for test in range(t):
    n=list(map(int,input()))
    if check(n):
        print("YES")
    else:
        print("NO")