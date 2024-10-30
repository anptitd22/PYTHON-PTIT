class race:
    def __init__(self,name,adress,time):
        self.name=name
        self.adress=adress
        self.time=time
        self.record=0
        self.id=""
        a=self.adress.split()
        a+=self.name.split()
        for i in range(len(a)):
            self.id+=a[i][:1]
        a=list(map(int,time.split(":")))
        self.record=120/float((a[0]-6)+(a[1]/60))
    def __str__(self):
        return self.id+' '+self.name+' '+self.adress+f' {self.record:.0f} Km/h'
a=[]
for t in range(int(input())):
    a.append(race(input(),input(),input()))
a.sort(key=lambda x: -x.record)
for x in a:
    print(x)