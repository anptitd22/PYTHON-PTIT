f=[0]*94
def fibo():
    f[0]=f[1]=1
    for i in range(2,94):
        f[i]=f[i-1]+f[i-2]
fibo()
for t in range(int(input())):
    a,b=map(int,input().split())
    for i in range(a-1,b):
        print(f[i],end=' ')
    print()