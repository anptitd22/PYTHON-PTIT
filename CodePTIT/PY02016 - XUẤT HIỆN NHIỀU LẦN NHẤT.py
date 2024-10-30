for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d=dict({})
    d2=dict({})
    cnt=0
    a.sort()
    for i in range(n):
        if a[i] in d:
            d[a[i]]+=1
        else:
            d[a[i]]=1
        if cnt<d[a[i]]:       
            cnt=d[a[i]]
            d2[cnt]=a[i]
    if cnt>n/2:
        print(d2[cnt])
    else:
        print("NO")