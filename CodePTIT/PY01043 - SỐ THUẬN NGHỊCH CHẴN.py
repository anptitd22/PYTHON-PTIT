def check(n):
    if len(n)%2==1: return False
    l=0
    r=len(n)-1
    while l<r:
        if n[l]!=n[r] or (ord(n[l])-ord('0'))%2!=0 or (ord(n[r])-ord('0'))%2!=0:
            return False
        l+=1
        r-=1
    return True
t=int(input())
for test in range(t):
    n=int(input())
    for i in range(22,n,2):
        if check(str(i)):
            print(i,end=' ')
    print()