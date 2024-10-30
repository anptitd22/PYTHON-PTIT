import math
pri=[True]*(10**6+1)
d1=[]
def prime():
    pri[0]=pri[1]=False
    for i in range(2,math.isqrt(10**6)+1):
        if pri[i]:
            for j in range(i*i,10**6+1,i):
                pri[j]=False
    for i in range(13,10**6+1):
        if pri[i]:
            d1.append(i)
prime()
def dao(n):
    res=0
    while n>0:
        res=res*10+n%10
        n//=10
    return res
for t in range(int(input())):
    d2=dict({})
    n=int(input())
    for i in range(0,len(d1)):
        a=dao(d1[i])
        if d1[i]>=n:
            break
        if a>=n:
            continue
        if d1[i]!=a and pri[a] and (not d1[i] in d2):
            print(d1[i],a,end=' ')
            d2[a]=1
    print()