import math
t=int(input())
for test in range(t):
    n=input()
    maxx=10**18
    cnt=0
    for i in range(0,len(n)):
        if n[i].isalpha():
            if i!=0 and n[i-1].isdigit():
                maxx=min(cnt,maxx)
                cnt=0
        else:
            cnt=cnt*10+int(n[i])
    print(maxx)