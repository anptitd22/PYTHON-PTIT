import math
pri=[True]*(10**5+1)
f,a=[],[]
pri[0]=pri[1]=False
for i in range(2,math.isqrt(10**5+1)):
    if pri[i]:
        f.append(i)
        for j in range(i*i,10**5+1,i):
            pri[j]=False
for i in range(math.isqrt(10**5),10**5+1):
    if pri[i]:
        f.append(i)
for i in range(len(f)):
    if f[i]**8<=10**9:
        a.append(f[i]**8)
    for j in range(i+1,len(f)):
        res=(f[i]**2)*(f[j]**2)
        if res<=10**9:
            a.append(res)
        else:
            break
a.sort()
def upper_bow(l, r, x):
    if l==r: return l
    mid = (l+r)//2
    if a[mid] <= x: return upper_bow(mid+1, r, x)
    return upper_bow(l, mid, x)
print(upper_bow(0, len(a)-1, int(input())))