d=dict({})
for t in range(int(input())):
    a=input().split()
    if a[3]=="IN":
        if not a[4] in d:
            d[a[4]]=0
        if a[2]=="5":
            d[a[4]]+=10000
        elif a[2]=="7":
            d[a[4]]+=15000
        elif a[2]=="2":
            d[a[4]]+=20000
        elif a[2]=="29":
            d[a[4]]+=50000
        else:
            d[a[4]]+=70000
for x,y in d.items():
    print(x,y,sep=": ")