import math
def sum_digit(n):
    if n==0 : return 0
    return n%10+sum_digit(n//10)
def nto(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return n>1
t=int(input())
for test in range(t):
    n=int(input())
    if nto(sum_digit(n)):
        print("YES")
    else:
        print("NO")