mod=int(1e9+7)
def findk(n, k):
    global mod
    ans = 0
    res = 1
    while (k > 0):
        if ((k & 1) == 1) :
            ans = ans + res
            ans%=mod
        res = (res * n)%mod
        k = k // 2
    return ans
for t in range(int(input())):
    n,k=map(int,input().split())
    print(findk(n,k))