def cs(n,m):
    if n==0:
        return
    cs(n//m,m)
    if n%m>=10:
        print(chr(65+n%m-10),end='')
    else: print(n%m,end='')
for t in range(int(input())):
    n,m=map(int,input().split())
    cs(n,m)
    print()