for t in range(int(input())):
    n=int(input())
    u=float(input())
    p=list(map(float,input().split()))
    if(u>0):
        d=p
        avg1=sum(p)/n
        avg2=avg1+u/n
        if avg2>=1:
            print('%.6f'%1)
            continue
        mul=1.0
        c=n
        while True:
            a,d2=[],[]
            for i in d:
                if i<=avg2:
                    d2.append(i)
                else:
                    a.append(i)
            if len(a)==0:
                break
            c-=len(a)
            avg2=(sum(d2)+u)/c
            d=d2
        for i in range(n):
            mul*=max(p[i],avg2)
        print("%.6f"%mul)
    elif u<0:
        d=p
        avg1=sum(p)/n
        avg2=avg1+u/n
        if avg2<=0:
            print('%.6f'%0)
            continue
        mul=1.0
        c=n
        while True:
            a,d2=[],[]
            for i in d:
                if i>=avg2:
                    d2.append(i)
                else:
                    a.append(i)
            if len(a)==0:
                break
            c-=len(a)
            avg2=(sum(d2)+u)/c
            d=d2
        for i in range(n):
            mul*=min(p[i],avg2)
        print("%.6f"%mul)
    else:
        mul=1.0
        for i in range(n):
            mul*=p[i]
        print("%.6f"%mul)