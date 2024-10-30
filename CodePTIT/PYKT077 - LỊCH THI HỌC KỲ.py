from functools import cmp_to_key
d=dict({})
class semester:
    def __init__(self,id,code,date,time,group):
        self.id='T'+format(id,'03d')
        self.code=code
        self.subject=d[code]
        self.date=date
        self.time=time
        self.gruop=group
    def __str__(self):
        return self.id+' '+self.code+' '+self.subject+' '+self.date+' '+self.time+' '+self.gruop
def cmp(a,b):
    ac1=list(map(int,a.date.split('/')))
    ac2=list(map(int,b.date.split('/')))
    for i in range(len(ac1)-1,-1,-1):
        if ac1[i]!=ac2[i]:
            return ac1[i]-ac2[i]
    ac1=list(map(int,a.time.split(':')))
    ac2=list(map(int,b.time.split(':')))
    for i in range(len(ac1)):
        if ac1[i]!=ac2[i]:
            return ac1[i]-ac2[i]
    if a.code>=b.code:
        return 1
    else:
        return -1
n,m=map(int,input().split())
for i in range(n):
    s=input()
    t=input()
    d[s]=t
a=[]
for i in range(m):
    code,date,time,group=input().split()
    a.append(semester(i+1,code,date,time,group))
a.sort(key=cmp_to_key(cmp))
for x in a:
    print(x)