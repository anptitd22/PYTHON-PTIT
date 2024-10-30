class Student:
    def __init__(self,id,name,code,informatics,expertise):
        self.name=name
        self.id='GV'+format(id,'02d')
        self.informatics=informatics
        self.expertise=expertise
        self.score=self.informatics*2+self.expertise
        self.subject=""
        self.status=""
        if code[:1]=="A":
            self.subject="TOAN"
        elif code[:1]=="B":
            self.subject="LY"
        else:
            self.subject="HOA"
        if code[1:2]=="1":
            self.score+=2
        elif code[1:2]=="2":
            self.score+=1.5
        elif code[1:2]=="3":
            self.score+=1
        else:
            self.score+=0
        if self.score>=18:
            self.status='TRUNG TUYEN'
        else:
            self.status='LOAI'
    def __str__(self):
        return self.id+' '+self.name+' '+self.subject+f' {self.score:.1f} '+self.status
a=[]
for t in range(int(input())):
    a.append(Student(t+1,input(),input(),float(input()),float(input())))
a.sort(key= lambda x : -x.score)
for x in a:
    print(x)