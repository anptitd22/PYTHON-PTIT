import math
def nto(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return n>1
def check(a):
    tong=0
    for i in range(0,len(a),2):
        if i!=len(a)-1:
            tong+=a[i]+a[i+1]
            if a[i]%2!=0 or a[i+1]%2!=1:
                return False
        else:
            tong+=a[i]
            if a[i]%2!=0:
                return False
    return nto(tong)
t=int(input())
for test in range(t):
    n=list(map(int,input()))
    if check(n):
        print("YES")
    else:
        print("NO")