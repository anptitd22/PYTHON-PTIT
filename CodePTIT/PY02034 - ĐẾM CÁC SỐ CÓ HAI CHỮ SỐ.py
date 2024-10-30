n=input()
d=dict({})
if len(n)%2==1:
    n=n[:len(n)-1]
for i in range(0,len(n),2):
    if not n[i:i+2] in d:
        d[n[i:i+2]]=1
    else:
        d[n[i:i+2]]+=1
for x,y in d.items():
    print(x,y)