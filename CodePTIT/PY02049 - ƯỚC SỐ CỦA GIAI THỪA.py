for t in range(int(input())):
    n,m=map(int,input().split())
    cnt=0
    for i in range(m,n+1):
        while i%m==0:
            i/=m
            cnt+=1
    print(cnt)