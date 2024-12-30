class Subject:
    def __init__(self,id,name,type):
        self.id=id
        self.name=name
        self.type=type
    def __str__(self):
        return self.id+" "+self.name+" "+self.type
if __name__ == '__main__':
    a=[]
    for _ in range(int(input())):
        a.append(Subject(input(),input(),input()))
    a.sort(key=lambda x:x.id)
    for x in a:
        print(x)