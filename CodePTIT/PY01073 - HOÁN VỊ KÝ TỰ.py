x=[i for i in range(10)]
check=[True]*10
def result():
    for i in range(1,n+1):
        print(a[x[i]-1],end='')
    print()
def sinh(i):
    global x,n
    for j in range(1,n+1):
        if check[j]:
            check[j]=False
            x[i]=j
            if i==n:
                result()
            else:
                sinh(i+1)
            check[j]=True
a=input()
n=len(a)
sinh(1)