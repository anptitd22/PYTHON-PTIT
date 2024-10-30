for t in range(int(input())):
    a=[]
    n,m,l=map(int,input().split())
    a.append([0 for _ in range(m+1)])
    for i in range(n):
        b=list(map(int,input().split()))
        b.insert(0,0)
        a.append(b)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1:
                a[i][j]+=a[i][j-1]
            elif j==1:
                a[i][j]+=a[i-1][j]
            else:
                a[i][j]+=a[i-1][j]+a[i][j-1]-a[i-1][j-1]
    for i in range(n-l+1):
        for j in range(m-l+1):
            tong=a[i+l][j+l]-a[i+l][j]-a[i][j+l]+a[i][j]
            print(tong//(l**2),end=' ')
        print()        
    # for x in a:
    #     for y in x:
    #         print(y,end=' ')
    #     print()