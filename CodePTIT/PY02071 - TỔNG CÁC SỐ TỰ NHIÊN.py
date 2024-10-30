def tong(i,k,b):
    global a
    if k==0:
        a.append(list(b))
        return 
    for j in range(i,0,-1):
        if k>=j:
            b.append(j)
            tong(j,k-j,b)
            b.pop()
for t in range(int(input())):
    a=[]
    n=int(input())
    tong(n,n,list({})) 
    print(len(a))
    for x in a:
        print('(',end='')
        for i in range(0,len(x)-1):
            print(x[i],end=' ')
        print(x.pop(),')',sep='',end=' ')
    print()