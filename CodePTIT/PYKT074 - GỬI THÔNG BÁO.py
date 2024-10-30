for t in range(int(input())):
    a=list(input().split())
    s=a[0]
    for i in range(1,len(a)):
        if len(s)+len(a[i])+1>100: break
        s+=" "+a[i]
    print(s)