def check(n,m):
    if len(n)!=len(m):
        return False
    else:
        n.sort()
        m.sort()
        for i in range(len(n)):
            if n[i]!=m[i]:
                return False
        return True
for t in range(int(input())):
    n=list(input())
    m=list(input())
    if check(n,m):
        print("Test ",t+1,": YES",sep='')
    else:
        print("Test ",t+1,": NO",sep='')