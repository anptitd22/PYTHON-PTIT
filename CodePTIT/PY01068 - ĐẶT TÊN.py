def sinh(i,cnt,n,k,a):
    for j in range(i,len(n)):
        a[cnt]=n[j]
        if cnt==k-1:
            for x in a:
                print(x,end=' ')
            print()
        else:
            if j<len(n)-1:
                sinh(j+1,cnt+1,n,k,a)
n,k=map(int,input().split())
st=set(input().split())
b=list(st)
b.sort()
a=[0]*k
sinh(0,0,b,k,a)