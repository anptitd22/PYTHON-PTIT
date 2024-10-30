from functools import cmp_to_key
d=dict({})
class Filmlist:
    def __init__(self,id,type,lauch_date,name,ep):
        self.id="P"+format(id,'03d')
        self.type=d[type]
        self.lauch_date=lauch_date
        self.name=name
        self.ep=ep
    def __str__(self):
        return self.id+' '+self.type+' '+self.lauch_date+' '+self.name+' '+f'{self.ep}'
def cmp(a,b):
    ac1=list(map(int,a.lauch_date.split("/")))
    ac2=list(map(int,b.lauch_date.split('/')))
    for i in range(2,-1,-1):
        if ac1[i]!=ac2[i]:
            return ac1[i]-ac2[i]
    if a.name>b.name:
        return 1
    else:
        return b.ep-a.ep
n,m=map(int,input().split())
for i in range(1,n+1):
    s=input()
    d['TL'+format(i,'03d')]=s
a=[]
for i in range(m):
    a.append(Filmlist(i+1,input(),input(),input(),int(input())))
a.sort(key=cmp_to_key(cmp))
for x in a:
    print(x)