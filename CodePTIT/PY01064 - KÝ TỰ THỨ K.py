def check(n):
    if n % 2==1:
        return 0
    else:
        return 1+check(n//2)
for t in range(int(input())):
    n,k=map(int,input().split())
    print(chr(65+check(k)))