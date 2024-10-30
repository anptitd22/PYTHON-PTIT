def check(a,b,c,ok):
    i,j,k=0,0,0
    while i < len(a) and j <len(b) and k<len(c):
        if a[i]==b[j] and a[i]==c[k]:
            ok=0
            print(a[i],end=' ')
            i+=1
            j+=1
            k+=1
        elif a[i]<b[j]:
            i+=1
        elif b[j]<c[k]:
            j+=1
        else:
            k+=1
    if ok==1:
        print("NO",end='')       
for t in range(int(input())):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    check(a,b,c,1)
    print()