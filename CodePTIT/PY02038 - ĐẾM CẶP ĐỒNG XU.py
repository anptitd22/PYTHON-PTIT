t=int(input())
a=[]
for i in range(t):
    b=list(input())
    a.append(b)
cap=[[0 for _ in range(t)]for _ in range(t)]
tong=0
for i in range(t):
    for j in range(t):
        if j+1<t:
            for k in range(j+1,t):
                if a[i][j]=='C' and a[i][k]==a[i][j]:
                    cap[i][j]+=1
        if i+1<t:
            for l in range(i+1,t):
                if a[i][j]=='C' and a[l][j]==a[i][j]:
                    cap[i][j]+=1
    tong+=sum(cap[i])
print(tong)