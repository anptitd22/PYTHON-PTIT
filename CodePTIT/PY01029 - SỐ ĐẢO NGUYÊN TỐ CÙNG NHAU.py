import math
t=int(input())
for test in range(t):
    n=input()
    m=n[::-1]
    n=int(n)
    m=int(m)
    if math.gcd(n,m)==1:
        print("YES")
    else:
        print("NO")