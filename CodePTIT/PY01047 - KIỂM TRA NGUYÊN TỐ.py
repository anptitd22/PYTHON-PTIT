import math
def nto(n):
    if n<2: return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return True
t=int(input())
for test in range(t):
    n=input()
    s=''
    for i in range(len(n)-1,len(n)-5,-1):
        s=n[i]+s
    if nto(int(s)):
        print("YES")
    else:
        print("NO")