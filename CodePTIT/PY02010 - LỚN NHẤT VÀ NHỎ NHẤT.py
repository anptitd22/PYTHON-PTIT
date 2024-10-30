while True:
    t=int(input())
    if t==0:
        break
    minn,maxx=1e100+1,0
    for test in range(t):
        n=int(input())
        minn=min(minn,n)
        maxx=max(maxx,n)
    if maxx==minn:
        print("BANG NHAU")
    else:
        print(minn,maxx)