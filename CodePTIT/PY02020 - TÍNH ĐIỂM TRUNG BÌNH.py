n=int(input())
a=list(map(float,input().split()))
maxx,minn=-1,11
d=dict({})
for i in a:
    if i>maxx:
        maxx=i
    if i<minn:
        minn=i
sum1,cnt=0,0
for i in a:
    if i!=maxx and i!=minn:
        sum1+=i
        cnt+=1
print('%.2f'%(sum1/cnt))