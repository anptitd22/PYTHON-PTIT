for t in range(int(input())):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    b=[0]*n
    d%=n
    d=n-d
    for i in range(n):
        b[(i+d)%n]=a[i]
    for x in b:
        print(x,end=' ')
    print()