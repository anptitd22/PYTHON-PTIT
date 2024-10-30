for t in range(int(input())):
    n=int(input())
    a,c,b=map(int,input().split())
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=a
    for i in range(2,n+1):
        if i%2==1:
            dp[i]=min(dp[i-1]+a,dp[(i+1)//2]+b+c)
        else:
            dp[i]=min(dp[i-1]+a,dp[i//2]+b)
    print(dp[n])