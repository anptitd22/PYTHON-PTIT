dau=["+","-"]
ok=0
def check(n,s):
    x=int(n[0]+n[1])
    if s[0]!="0" and x<10:
        return False
    y=int(n[5]+n[6])
    if s[5]!="0" and y<10:
        return False
    z=int(n[10]+n[11])
    if s[10]!="0" and z<10:
        return False
    if n[3]=="-":
        return x-y==z
    else:
        return x+y==z
def Try(i,res,s):
    global ok
    if ok==1:
        return
    if i==len(s):
        if check(res,s):
            print(res)
            ok=1
        return
    if s[i]=="?":
        if i==3:
            for j in dau:
                Try(i+1,res+j,s)
        elif i==8:
            Try(i+1,res+"=",s)
        else:
            for j in range(0,10):
                Try(i+1,res+str(j),s)
    else:
        Try(i+1,res+s[i],s)
for t in range(int(input())):
    ok=0
    res=input().split()
    s=' '.join(res)
    if s[3]=="/" or s[3]=="*":
        print("WRONG PROBLEM!")
    else:
        Try(0,"",s)
        if ok==0:
            print("WRONG PROBLEM!")