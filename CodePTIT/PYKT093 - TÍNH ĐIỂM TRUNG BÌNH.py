import math
d=dict({})
class Student:
    def __init__(self,id,name,sub1,sub2,sub3):
        self.id='SV'+format(id,'02d')
        a=name.split()
        self.name=' '.join(a).title()
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.score=(sub1*3+sub2*3+sub3*2)/8
        self.score*=100
        if self.score-int(self.score)>=0.5:
            self.score=math.ceil(self.score)
        self.score/=100
    def __str__(self):
        return self.id+' '+self.name+' '+f'{self.score:.2f}'
a=[]
for i in range(int(input())):
    a.append(Student(i+1,input().strip(),float(input()),float(input()),float(input())))
a.sort(key=lambda x: -x.score)
cnt=1
for x in a:
    if x.score in d:
        print(x,d[x.score])
    else:
        d[x.score]=cnt
        print(x,d[x.score])
    cnt+=1