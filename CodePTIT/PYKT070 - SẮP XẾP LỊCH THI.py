from datetime import datetime
class subject:
    def __init__(self,id,name,type):
        self.id=id
        self.name=name
        self.type=type
class date:
    def __init__(self,id,day,time,room):
        self.id="C"+format(id,"03d")
        self.day = day
        self.time = time
        self.room = room
class schedule:
    def __init__(self,date,subject,gr,num):
        self.subject=subject
        self.date=date
        self.time1=datetime.timestamp(datetime.strptime(date.day+" "+date.time,'%d/%m/%Y %H:%M'))
        self.gr=gr
        self.num=num
    def __str__(self):
        return self.date.day+" "+self.date.time+" "+self.date.room+" "+self.subject.name+" "+self.gr+" "+self.num
if __name__ == '__main__':
    d=dict()
    d2=dict()
    try:
        f1=open("MONTHI.in","r")
        f2=open("CATHI.in","r")
        f3=open("LICHTHI.in","r")
        for t in range(int(f1.readline().strip())):
            s=subject(f1.readline().strip(),f1.readline().strip(),f1.readline().strip())
            d[s.id]=s
        f1.close()
        for t in range(int(f2.readline().strip())):
            s=date(t+1,f2.readline().strip(),f2.readline().strip(),f2.readline().strip())
            d2[s.id]=s
        f2.close()
        a=[]
        for t in range(int(f3.readline().strip())):
            x,y,z,t=map(str,f3.readline().strip().split())
            a.append(schedule(d2.get(x),d.get(y),z,t))
            a.sort(key=lambda x: (x.time1,x.date.id))
        for x in a:
            print(x)
        f3.close
    except FileNotFoundError:
        print()
    except IOError:
        print()