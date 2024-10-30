def solv(n):
    tong=0
    tich=1.1
    for i in range(0,len(n)):
        if i %2==1:
            tong+=n[i]
        else:
            if n[i]!=0:
                tich=int(tich)*n[i]
    if tich==1.1:   
        print(0,tong)
    else:
        print(tich,tong)
t=int(input())        
for test in range(t):
    n=list(map(int,input()))
    solv(n)