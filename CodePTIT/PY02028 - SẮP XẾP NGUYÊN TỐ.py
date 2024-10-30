import math
def check(x):
    for i in range(2,math.isqrt(x)+1):
        if x%i==0:
            return False
    return x>1
n=int(input())
a=list(map(int,input().split()))
res=[0]*len(a)
s=[]
for i in range(len(a)):
    if check(a[i]):
        res[i]=1
        s.append(a[i])
s.sort(reverse=True)
for i in range(len(res)):
    if res[i]==0:
        print(a[i],end=' ')
    else:
        print(s.pop(),end=' ')