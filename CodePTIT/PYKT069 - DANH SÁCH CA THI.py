import time
class Semester:
    def __init__(self,id,day,stime,room):
        self.id="C"+format(id,'03d')
        self.day=day
        self.stime=stime
        self.room=room
        s=day+" "+stime
        self.time1=time.mktime(time.strptime(s,"%d/%m/%Y %H:%M"))
    def __str__(self):
        return self.id+" "+self.day+" "+self.stime+" "+self.room
if __name__ == '__main__':
    f=open("CATHI.in","r")
    a=[]
    n=int(f.readline().strip())
    for t in range(n):
        a.append(Semester(t+1,f.readline().strip(),f.readline().strip(),f.readline().strip()))
    a.sort(key=lambda x: x.time1)
    for x in a:
        print(x)