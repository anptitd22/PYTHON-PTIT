a=[]
for t in range(int(input())):
    s=input()
    ok,res=0,0
    for i in range(len(s)):
        if s[i].isdigit():
            ok=1
            res=res*10+(ord(s[i])-ord('0'))
            if i==len(s)-1:
                a.append(res)
        else:
            if ok==1:
                a.append(res)
                ok=0
            res=0
a.sort()
for x in a:
    print(x)