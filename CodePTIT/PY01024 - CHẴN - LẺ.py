def check(n):
    res=n%10
    n//=10
    sum=res
    while n>0:
        if n%10-res!=2 and res-n%10!=2:
            return False
        sum+=n%10
        res=n%10
        n//=10
    return sum%10==0 
t=int(input())
for test in range(t):
    n=int(input())
    if check(n):
        print("YES")
    else:
        print("NO")