import math
def check(n):
    res,sum=n,0
    while res>0:
        sum+=math.factorial(res%10)
        res//=10
    return sum==n
for t in range(int(input())):
    n=int(input())
    if check(n):
        print("Yes")
    else:
        print("No")