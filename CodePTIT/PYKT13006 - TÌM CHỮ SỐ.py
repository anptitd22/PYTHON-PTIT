class thapphan:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __mul__(self, other):
        s=thapphan(0,0)
        s.x = (self.x * other.x + 5 * self.y * other.y) % 1000
        s.y = (self.x * other.y + self.y * other.x) % 1000
        return s
def pow(a,b):
    if b==0: return thapphan(1,0)
    if b%2==1: return pow(a,b-1)*a
    res=pow(a,b//2)
    return res*res
for t in range(int(input())):
    n=int(input())
    x=thapphan(3,1)
    a=pow(x,n)
    b=f"Case #{t+1}: "+format(int(a.x*2%1000-1),'03d')
    print(b)
#bai nay bua vai loz