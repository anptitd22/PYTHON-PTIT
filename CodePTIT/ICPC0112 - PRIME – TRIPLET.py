import math
pri=[True]*(10**6+1)
tri=[0]*(10**6+8)
def prime():
    pri[0]=pri[1]=False
    for i in range(2,math.isqrt(10**6)):
        if pri[i]:
            for j in range(i*i,10**6+1,i):
                pri[j]=False
    for i in range(5,10**6+1):
        if pri[i] and pri[i+2] and pri[i+6]:
            tri[i+7]+=1
        if pri[i] and pri[i+4] and pri[i+6]:
            tri[i+7]+=1
        tri[i]+=tri[i-1]
prime()
for i in range(int(input())):
    print(tri[int(input())])