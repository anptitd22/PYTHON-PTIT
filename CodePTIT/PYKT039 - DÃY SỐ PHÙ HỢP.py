def check(a,b):
    for i in range(len(a)):
        if a[i]>b[i]:
            return False
    return True
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    if check(a,b):
        print("YES")
    else:
        print("NO")