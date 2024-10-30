arr=[[10,12,14,20],[10,11,13,16],[9,10,12,14],[8,9,11,13]]
d=dict({})
class eployee:
    def __init__(self,id,name,unit_salary,day):
        self.id=id
        self.name=name
        self.unit_salary=unit_salary
        self.day=day
        self.coefficient=0
        self.team=d[id[3:5]]
        res1,res2=int(id[1:3]),id[:1]
        if res1<=3:
            self.coefficient=arr[ord(res2)-ord('A')][0]
        elif res1<=8:
            self.coefficient=arr[ord(res2)-ord('A')][1]
        elif res1<=15:
            self.coefficient=arr[ord(res2)-ord('A')][2]
        else:
            self.coefficient=arr[ord(res2)-ord('A')][3]
        self.salary=self.unit_salary*self.coefficient*self.day
    def __str__(self):
        return self.id+' '+self.name+' '+self.team+' '+f'{self.salary*1000}'
a=[]
for i in range(int(input())):
    s,*t=input().split()
    t=' '.join(t)
    d[s]=t
for i in range(int(input())):
    a.append(eployee(input(),input(),int(input()),int(input())))
for x in a:
    print(x)