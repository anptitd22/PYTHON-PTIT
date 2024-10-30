for t in range(int(input())):
    n=int(input())
    cnt,a,b=0,1,1
    while a>=1:
        # if b%2==0:
        #     a=(n/(b+1))-b/2
        # else:
        #     (2*a+b)*(b+1)//2+(2*a+b)=
        a=(n/(b+1))-b/2
        if a==int(a) and a>=1:
            cnt+=1
        b+=1
    print(cnt)