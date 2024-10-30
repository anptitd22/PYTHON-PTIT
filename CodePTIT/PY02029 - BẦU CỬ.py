n,k=map(int,input().split())
a=list(map(int,input().split()))
cnt=[0]*(k+1)
maxx1,maxx2=0,0
for i in range(len(a)-1):
    if cnt[a[i]]==0:
        cnt[a[i]]=1
        for j in range(i+1,len(a)):
            if a[j]==a[i]:
                cnt[a[i]]+=1
        if cnt[a[i]]>maxx2:
            maxx1=maxx2
            maxx2=cnt[a[i]]
        elif cnt[a[i]]>maxx1 and cnt[a[i]]<maxx2:
            maxx1=cnt[a[i]]
if maxx1==0:
    print("NONE")
else:
    for i in range(k+1):
        if cnt[i]==maxx1:
            print(i)
            break