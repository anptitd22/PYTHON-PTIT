import math
def nto(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return n>1
n,m=map(int,input().split())
a=[]
maxx,check=-1e9,0
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
    b=[x for x in b if nto(x)]
    if len(b)!=0:
        check=1
        maxx=max(max(b),maxx)
if check==0:
    print("NOT FOUND")
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if a[i][j]==maxx:
                print(f'Vi tri [{i}][{j}]')