for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    r,l=0,1e3+1
    st=set({})
    for x in a:
        st.add(x)
        r=max(r,x)
        l=min(l,x)
    print((r-l+1)-len(st))