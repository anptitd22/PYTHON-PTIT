def solv(n):
    tong=0
    tich=res=1.1
    for i in range(0,len(n)):
        if i %2==0:
            tong+=n[i]
        else:
            if n[i]!=0:
                tich=int(tich)*n[i]
    if tich==res:   
        print(tong,0)
    else:
        print(tong,tich)
t=int(input())        
for test in range(t):
    n=list(map(int,input()))
    solv(n)