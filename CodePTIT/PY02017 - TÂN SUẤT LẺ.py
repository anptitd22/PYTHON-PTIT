from collections import Counter
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=dict(Counter(a))
    for i in range(len(a)):
        if b[a[i]]%2==1:
            print(a[i])
            break