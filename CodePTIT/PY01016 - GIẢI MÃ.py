import math
t=int(input())
for test in range(t):
    n=input()
    for i in range(len(n)):
        if i%2==1:
            res=int(n[i])
            while res>0:
                print(n[i-1],end='')
                res-=1
    print()