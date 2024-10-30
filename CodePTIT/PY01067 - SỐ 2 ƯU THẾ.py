for t in range(int(input())):
    n=int(input())
    a=['2','1']
    b=[]
    while len(b)<n:
        x=a.pop()
        if x.count('2')>len(x)/2:
            b.append(x)
        s1=x+'0'
        s2=x+'1'
        s3=x+'2'
        a.insert(0,s1)
        a.insert(0,s2)
        a.insert(0,s3)
    for x in b:
        print(x,end=' ')
    print()