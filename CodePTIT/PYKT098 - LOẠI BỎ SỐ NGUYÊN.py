try:
    f=open("DATA.in","r")
    a=f.read().split()
    b=[]
    for x in a:
        if not x.isdigit() or (x.isdigit() and int(x)>2**31-1):
            b.append(x)
    b.sort()
    for x in b:
        print(x,end=' ')
except FileNotFoundError:
    print()