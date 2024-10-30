def he8(n):
    if n==0:
        return
    he8(n//8)
    print(n%8,end='')
n=input()
res=0
for i in n:
    res=res*2+int(i)
he8(res)