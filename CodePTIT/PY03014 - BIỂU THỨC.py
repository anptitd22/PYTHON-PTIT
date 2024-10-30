for t in range(int(input())):
    s=input()
    a,b,cnt=[],[],1
    for i in s:
        if i=="(":
            a.append(cnt)
            b.append(cnt)
            cnt+=1
        elif i==")":
            b.append(a.pop())
        else:
            continue
    for x in b:
        print(x,end=' ')
    print()