import math
t=int(input())
for test in range(t):
    n=input()
    cnt=1
    for i in range(len(n)):
        if i==len(n)-1:
            print(cnt,n[i],sep='',end='')
            break
        if(n[i]!=n[i+1]):
            print(cnt,n[i],sep ='',end='')
            cnt=1
        else:
            cnt+=1
    print()