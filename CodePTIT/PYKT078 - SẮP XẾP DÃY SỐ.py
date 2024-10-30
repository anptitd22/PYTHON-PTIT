for t in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b,c=[],[]
    cnt,idx=-1e9-1,1
    for i in range(n):
        if cnt<a[i]:
            if cnt<0:
                idx=len(b)
            else:
                idx=len(c)
            cnt=a[i]
        if a[i]<0:
            b.append(a[i])
        else:
            c.append(a[i])
    if cnt<0:
        b.insert(idx,m)
    else:
        c.insert(idx,m)
    for i in b:
        print(i,end=' ')
    for i in c:
        print(i,end=' ')
    print()