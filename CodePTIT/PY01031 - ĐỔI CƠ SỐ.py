def hek(n,k):
    if n==0:
        return
    hek(n//k,k)
    if n%k>=10:
        print(chr(55+n%k),end='')
    else:
        print(n%k,end='')
for t in range(int(input())):
    n,k=map(int,input().split())
    hek(n,k)
    print()