while True:
    a=input()
    if '0' in a and '10' not in a:
        break
    k,n=a.split()
    k=int(k)
    p='ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    s=''
    for i in range(0,len(n)):
        s=p[(p.index(n[i])+k)%28]+s
    print(s)