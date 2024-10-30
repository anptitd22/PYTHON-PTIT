n=int(input())
a=[]
while True:
    try: a.extend(map(int, input().split()))
    except: break
res=[0]*n
b=[]
c=[]
for i in range(len(a)):
    if a[i]%2==1:
        res[i]=1
        b.append(a[i])
    else:
        c.append(a[i])
b.sort()
c.sort(reverse=True)
for i in range(n):
    if res[i]==1:
        print(b[len(b)-1],end=' ')
        b.pop()
    else:
        print(c[len(c)-1],end=' ')
        c.pop()