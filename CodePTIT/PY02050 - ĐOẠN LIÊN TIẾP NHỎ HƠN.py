for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for i in range(len(a)):
        while len(b)!=0 and a[b[len(b)-1]]<=a[i]:
            b.pop()
        if len(b)==0:
            print(i+1,end=' ')
        else:
            print(i-b[len(b)-1],end=' ')
        b.append(i)
    print()