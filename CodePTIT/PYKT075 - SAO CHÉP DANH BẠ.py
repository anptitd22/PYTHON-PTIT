from sys import stdin
class phonebook:
    def __init__(self,name,number,day):
        s=name.split()
        self.name=' '.join(s).title()
        self.number=number
        self.day=day
        self.fname=self.name.split()[-1]
        self.mname=self.name.split()[:-1]
    def __str__(self):
        return self.name+": "+self.number+" "+self.day
# f2=open("DIENTHOAI.txt","w")
try: f1=open("SOTAY.txt","r")
except: f1=stdin
lines=[x.strip() for x in f1 if x.strip()!='']
a=[]
day=lines[0].split()[1]
i=1
while i<len(lines):
    s1=lines[i]
    i+=1
    if s1.count('/')>0:
        day = s1.split()[1]
        continue
    s2=lines[i]
    i+=1
    a.append(phonebook(s1.lower(),s2,day))
a.sort(key=lambda x: (x.fname,x.mname))
for x in a:
    # f2.write(x+'\n')
    print(x)