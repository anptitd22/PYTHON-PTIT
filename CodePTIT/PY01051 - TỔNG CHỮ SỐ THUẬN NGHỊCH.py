def sum_digit(n):
    if n==0: return 0
    return n%10+sum_digit(n//10)
def check(n):
    if len(n)==1: return False
    l=0
    r=len(n)-1
    while l<r:
        if n[l]!=n[r]:
            return False
        l+=1
        r-=1
    return True
t=int(input())
for test in range(t):
    n=int(input())
    a=list(map(int,str(sum_digit(n))))
    if check(a):
        print("YES")
    else:
        print("NO")