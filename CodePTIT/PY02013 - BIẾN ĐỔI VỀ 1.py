def bd1(n):
    if n==1: return 1
    if n%2==0: return 1+bd1(n//2)
    else: return 1+bd1(n*3+1)
while True:
    t=int(input())
    if t==0: break
    print(bd1(t))