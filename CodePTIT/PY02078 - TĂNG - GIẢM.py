for _ in range(int(input())):
    n=int(input())
    a=[]
    for _ in range(n):
        a.append(list(map(float,input().split())))
    b=[1]*n
    for i in range(1,n):
        for j in range(i):
            if a[i][0]>a[j][0] and a[i][1]<a[j][1]:
                b[i]=max(b[i],b[j]+1)
    print(max(b))