import math
t=int(input())
for test in range(t):
    n=input()
    maxx=0
    cnt=0
    n+='a'
    for i in range(0,len(n)):
        if n[i].isalpha():
            if i!=0 and n[i-1].isdigit():
                maxx=max(cnt,maxx)
                cnt=0
        else:
            cnt=cnt*10+int(n[i])
    print(maxx)