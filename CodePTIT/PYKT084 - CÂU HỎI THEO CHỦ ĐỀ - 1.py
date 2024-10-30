ok=1
res=""
d=dict({})
for t in range(int(input())):
    n=input()
    if len(n)==0:
        ok=1
    else:
        if ok==1:
            ok=0
            res=n
            d[res]=-1
        d[res]+=1
for x,y in d.items():
    print(x,y,sep=": ")  