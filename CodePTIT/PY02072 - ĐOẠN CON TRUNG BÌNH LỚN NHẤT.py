n=int(input())
a=list(map(int,input().split()))
b=max(a)
cnt,key=1,-1
for i in range(0,len(a)-1):
    if i<=key:
        continue
    if a[i]==b:
        for j in range(i+1,len(a)):
            if a[j]==a[i]:
                cnt=max(j-i+1,cnt)
                key=j
            else:
                break
print(cnt)