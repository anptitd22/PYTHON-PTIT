from math import *
t=int(input())
for test in range(t):
    n=int(input())
    res='1'
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            cnt=0
            while n%i==0:
                cnt+=1
                n//=i
            res+=' * '
            res+=str(i)+'^'+str(cnt)
    if n>1:
        res+=' * '
        res+=str(n)+'^1'
    print(res)