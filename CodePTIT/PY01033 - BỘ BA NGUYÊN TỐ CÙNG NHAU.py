import math
x,y=map(int,input().split())
for i in range(x,y-1):
    for j in range(i+1,y):
        if math.gcd(i,j)==1:
            for k in range(j+1,y+1):
                if math.gcd(i,k)==1 and math.gcd(j,k)==1:
                    print('(',i,', ',j,', ',k,')',sep='') 