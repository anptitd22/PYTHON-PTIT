import math
t=int(input())
for test in range(0,t):
    n=input()
    res=n[0]+n[1]
    res2=n[len(n)-2]+n[len(n)-1]
    if res==res2:
        print("YES")
    else:
        print("NO")