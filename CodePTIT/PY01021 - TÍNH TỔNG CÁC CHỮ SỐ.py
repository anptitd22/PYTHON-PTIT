for t in range(int(input())):
    s=input()
    sum1=0
    a=[]
    for x in s:
        if x.isdigit():
            sum1+=int(x)
        else:
            a.append(x)
    a.sort()
    print(''.join(a),sum1,sep='')