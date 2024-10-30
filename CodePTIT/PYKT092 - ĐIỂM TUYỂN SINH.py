class Student:
    def __init__(self,id,name,score,folk,district):
        self.id='TS'+format(id,'02d')
        a=name.split()
        self.name=' '.join(a).title()
        self.score=score
        self.folk=folk
        self.district=district
        self.status=""
        if self.district==1:
            self.score+=1.5
        elif self.district==2:
            self.score+=1
        else:
            self.score+=0
        if folk == "Kinh":
            self.score+=0
        else:
            self.score+=1.5
        if self.score>=20.5:
            self.status="Do"
        else:
            self.status="Truot"
    def __str__(self):
        return self.id+' '+self.name+' '+f'{self.score} '+self.status
a=[]      
for i in range(int(input())):    
    a.append(Student(i+1,input().strip(),float(input()),input(),int(input())))
a.sort(key=lambda x: -x.score)
for x in a:
    print(x)