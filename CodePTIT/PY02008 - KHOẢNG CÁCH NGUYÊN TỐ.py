import math
f=[0,2]
def nto(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return n>1
k=3
while len(f)<=1001:
    if nto(k):
        f.append(k)
    k+=2         
n,m=map(int,input().split())
for i in range(n+1):
    m+=f[i]
    print(m,end=' ')