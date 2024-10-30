n,m=map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
a=sorted(list(a))
b=sorted(list(b))
def canb():
    for i in range(len(a)):
        if a[i]!=b[i]:
            return 'NO'
    return 'YES'
print(canb())