import math
def score(n):
    if n>=39:
        return 9.0
    elif n>=37:
        return 8.5
    elif n>=35:
        return 8.0
    elif n>=33:
        return 7.5
    elif n>=30:
        return 7.0
    elif n>=27:
        return 6.5
    elif n>=23:
        return 6.0
    elif n>=20:
        return 5.5
    elif n>=16:
        return 5.0
    elif n>=13:
        return 4.5
    elif n>=10:
        return 4.0
    elif n>=7:
        return 3.5
    elif n>=5:
        return 3.0
    elif n>=3:
        return 2.5
    else:
        return 1.0
for t in range(int(input())):
    a,b,c,d=map(float,input().split())
    sum1=(score(a)+score(b)+c+d)/4
    s=sum1-int(sum1)
    if s<0.25:
        sum1=math.floor(sum1)
    elif s>=0.25 and s<0.75:
        sum1=0.5+int(sum1)*1.0
    else:
        sum1=float(math.ceil(sum1))
    print(sum1)