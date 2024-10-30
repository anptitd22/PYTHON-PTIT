def checkmonth(x,y):
    if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
        return 31
    elif x==2:
        if y%4==0 and not y%100==0:
            return 29
        else:
            return 28
    else:
        return 30
def checkyear(y):
    if y%4==0 and y%100!=0:
        return 366
    else:
        return 365
class bill:
    def __init__(self,number,name,room,checkin,checkout,service):
        self.id="KH"+format(number,'02d')
        self.name=name
        self.room=room
        self.checkin=checkin
        self.checkout=checkout
        self.service=service
        self.price=0
        self.day=1
        a=list(map(int,self.checkin.split('/')))
        b=list(map(int,self.checkout.split('/')))
        if a[0]!=b[0]:
            self.day+=b[0]-a[0]
        if a[1]!=b[1]:
            if a[1]>b[1]:
                for i in range(b[1],a[1]):
                    self.day-=checkmonth(i,a[1])
            else:
                for i in range(a[1],b[1]):
                    self.day+=checkmonth(i,a[1])
        if a[2]!=b[2]:
            for i in range(a[2],b[2]):
                self.day+=checkyear(i+1)  
        res=self.room//100
        if res == 1:
            self.price=25*self.day+self.service
        elif res==2:
            self.price=34*self.day+self.service 
        elif res==3:
            self.price=50*self.day+self.service
        else:
            self.price=80*self.day+self.service
    def __str__(self):
        return self.id+' '+self.name+' '+f'{self.room} {self.day} {self.price}' 
a=[]
for t in range(int(input())):
    a.append(bill(t+1,input(),int(input()),input(),input(),int(input())))
a.sort(key=lambda x: -x.price)
for x in a:
    print(x)