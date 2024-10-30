a=[0]*21
n,k=0,0
def result(b):
    for i in range(1,k+1):
        print(b[a[i]-1],end=' ')
    print()
def sinh(i,b):
    global a,n,k
    for j in range(a[i-1]+1,n-k+i+1):
        a[i]=j
        if i==k:
            result(b)
        else:
            sinh(i+1,b)    
n,k=map(int,input().split())
b=list(set(map(int,input().split())))
n=len(b)
b.sort()
sinh(1,b)