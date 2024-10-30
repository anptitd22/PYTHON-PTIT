for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    cnt=0
    for i in range(1,n):
        res=max(a[i-1]/a[i],a[i]/a[i-1])
        for j in range(1,7):
            if res<=(2**j):
                cnt+=j-1
                break
    print(cnt)