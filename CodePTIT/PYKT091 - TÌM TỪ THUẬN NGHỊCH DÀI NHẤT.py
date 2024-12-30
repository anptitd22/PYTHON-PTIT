import collections
max1=0
def check(s):
    global max1
    l,r=0,len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    max1=max(len(s),max1)
    return True
try:
    f=open("VANBAN.in","r")
    a=f.read().split()
    b=[x for x in list(dict(collections.Counter(a)).items()) if check(x[0])]
    for x,y in b:
        if len(x)==max1:
            print(x,y)
except FileNotFoundError:
    print()