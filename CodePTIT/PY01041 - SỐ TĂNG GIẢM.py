def check(n):
    if len(n)<3: return False
    for i in range(0,len(n)-1):
        if n[i]>n[i+1]:
            for j in range(i+1,len(n)):
                if n[j]>=n[j-1] :
                    return False
            break
        elif n[i]==n[i+1]:
            return False
    return True
t=int(input())
for test in range(t):
    a=list(map(int,input()))
    if check(a):
        print("YES")
    else:
        print("NO")