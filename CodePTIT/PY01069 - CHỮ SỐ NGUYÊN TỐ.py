# n=int(input())
# a=['7','5','3','2']
# b=['2','3','5','7']
# while len(a)!=0:
#     x=a.pop()
#     s=set(x)
#     if '2' in s and '3' in s and '5' in s and '7' in s and int(x)%2==1:
#         print(x)
#     for i in b:
#         x+=i
#         if len(x)<=n:
#             a.insert(0,x)
#         x=x[:-1]
s=[]
def nto(x,n,a,b,c,d):
    if a+b+c+d>n:
        return
    if a+b+c+d<=n and a>0 and b>0 and c>0 and d>0 and x%2==1:
        s.append(x)
    x=x*10+2
    nto(x,n,a+1,b,c,d)
    x//=10
    x=x*10+3
    nto(x,n,a,b+1,c,d)
    x//=10
    x=x*10+5
    nto(x,n,a,b,c+1,d)
    x//=10
    x=x*10+7
    nto(x,n,a,b,c,d+1)
    x//=10
n=int(input())
nto(0,n,0,0,0,0)
s.sort()
for x in s:
    print(x)