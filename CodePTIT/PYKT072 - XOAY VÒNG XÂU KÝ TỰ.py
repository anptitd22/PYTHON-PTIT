def check(a):
    minn=1e5
    for i in range(len(a)):
        cnt=0
        for j in range(len(a)):
            if len(a[j])!=len(a[i]):
                return -1
            if i!=j:
                res=a[j]
                while res!=a[i]:
                    res=res[1:]+res[:1]
                    cnt+=1
                    if res==a[j]:
                        return -1
        minn=min(minn,cnt)
    return minn
a=[]
for i in range(int(input())):
    a.append(input())
print(check(a))