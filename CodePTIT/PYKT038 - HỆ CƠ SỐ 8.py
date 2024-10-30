def he10(n):
    res=0
    for i in n:
        res=res*2+int(i)
    return res
def he8(n):
    if n==0:
        return
    he8(n//8)
    print(n%8,end='')
t=input()
he8(he10(t))