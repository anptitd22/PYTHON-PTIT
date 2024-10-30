n=int(input())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
k=int(input())
sum1,sum2=0,0
for i in range(n):
    for j in range(n):
        if j>i:
            sum1+=a[i][j]
        elif j<i:
            sum2+=a[i][j]
        else:
            continue
if abs(sum1-sum2)<=k:
    print("YES")
    print(abs(sum1-sum2))
else:
    print("NO")
    print(abs(sum1-sum2))               