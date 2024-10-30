import math
def bd(a,b,c,d):
    if a==b and c==a and d==a:
        return 0
    return 1+bd(abs(a-b),abs(b-c),abs(c-d),abs(d-a))
while True:
    a,b,c,d=map(int,input().split())
    if a==0 and b==0 and c==0 and d==0:
        break
    print(bd(a,b,c,d))