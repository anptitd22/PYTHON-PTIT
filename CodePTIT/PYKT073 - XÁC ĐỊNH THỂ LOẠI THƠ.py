a=[]
for t in range(int(input())):
    b=list(input().split())
    a.append(len(b))
c=[]
i=0
a.append(0)
while i < len(a)-1 :
    ok1=0
    while a[i]!=7 and a[i]!=0:
        ok1=1
        i+=1
    if ok1==1:
        c.append(1)
    while a[i]==7 and i<len(a):
        i+=4
        c.append(2)
print(len(c))
for x in c:
    print(x)