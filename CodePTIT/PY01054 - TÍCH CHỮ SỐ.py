def devi(n):
    if n==0: return 1
    if n%10==0:
        return 1*devi(n//10)
    else:
        return n%10*devi(n//10)
t=int(input())
for test in range(t):
    n=int(input())
    print(devi(n))