import math
def nto(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return n>1
t=int(input())
for test in range(t):
    n=input()
    if nto(int(n[0:3])) and nto(int(n[len(n)-3:len(n)])):
        print("YES")
    else:
        print("NO")