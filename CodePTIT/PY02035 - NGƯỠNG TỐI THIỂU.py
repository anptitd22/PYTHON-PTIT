n=input()
k=int(input())
a,d=[],dict({})
ok=0
if len(n)%2==1:
    n=n[:len(n)-1]
for i in range(0,len(n),2):
    if not n[i:i+2] in d:
        d[n[i:i+2]]=1
        a.append(n[i:i+2])
    else:
        d[n[i:i+2]]+=1
    if d[n[i:i+2]]>=k:
        ok=1
if ok==0:
    print("NOT FOUND")
else:
    a.sort()
    for x in a:
        if d[x]>=k:
            print(x,d[x])