import math
n,m=map(int,input().split())
cnt=0
for i in range(int(math.pow(10,m-1)),int(math.pow(10,m))):
    if cnt==10:
        print()
        cnt=0
    if math.gcd(n,i)==1:
        cnt+=1
        print(i,end=' ')