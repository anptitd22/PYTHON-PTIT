n=int(input())
a=[]
while True:
    try: a.extend(list(map(int,input().split())))
    except: break
maxx,ok=0,0
cnt=[0]*300
for i in range(len(a)):
    cnt[a[i]]=1
    maxx=max(a[i],maxx)
for i in range(1,maxx+1):
    if cnt[i]==0:
        ok=1
        print(i)
if ok==0:
    print("Excellent!")