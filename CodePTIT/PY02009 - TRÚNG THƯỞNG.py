for t in range(int(input())): 
    cnt=[0]*1000001  
    maxx,cnt1=0,0 
    for i in range(int(input())):        
        n=int(input())
        cnt[n]+=1
        cnt1=max(cnt1,cnt[n])
        maxx=max(maxx,n)
    for i in range(maxx+1):
        if cnt[i]==cnt1:
            print(i)
            break