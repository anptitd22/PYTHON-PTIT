t=int(input())
for test in range(t):
    n=int(input())
    sum=0
    for i in range(n,0,-2):
        if i==0: continue
        sum+=1.0/i
    print('%.6f'%sum)