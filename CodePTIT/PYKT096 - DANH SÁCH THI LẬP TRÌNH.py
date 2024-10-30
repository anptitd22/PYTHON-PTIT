d=dict({})
class candidate:
    def __init__(self,id,name,team):
        self.id='C'+format(id,'03d')
        self.name=name
        self.team=team
        self.nameteam=d[team][0]
        self.school=d[team][1]
    def __str__(self):
        return self.id+' '+self.name+' '+self.nameteam+' '+self.school
a=[]
for i in range(int(input())):
    s=input()
    t=input()
    d['Team'+format(i+1,'02d')]=[s,t]
for i in range(int(input())):
    a.append(candidate(i+1,input(),input()))      
a.sort(key=lambda x: x.name)
for x in a:
    print(x)