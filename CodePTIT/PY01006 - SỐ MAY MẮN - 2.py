import math
def check(n):
    while n>0:
        if n%10!=4 and n%10!=7:
            return False
        n//=10
    return True
t=int(input())
for test in range(0,t):
    n=int(input())
    if(check(n)):
        print("YES")
    else:
        print("NO")