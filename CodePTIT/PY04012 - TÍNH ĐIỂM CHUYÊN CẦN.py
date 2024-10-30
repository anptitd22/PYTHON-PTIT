d=dict({})
class SinhVien:
    def __init__(self,id,name,className):
        self.id=id
        self.name=name
        self.className=className
        self.cc=10
        d[self.id]=self.cc
    def __str__(self):
        return self.id+' '+self.name+' '+self.className
a=[]
for t in range(int(input())):
    a.append(SinhVien(input(),input(),input()))
for i in range(len(a)):
    r=input().split()
    for x in r[1]:
        if x=='m':
            d[r[0]]-=1
        elif x=='v':
            d[r[0]]-=2
    d[r[0]]=max(0,d[r[0]])
for x in a:
    print(x,d[x.id],end='')
    if d[x.id]==0:
        print(' KDDK',end='')
    print()