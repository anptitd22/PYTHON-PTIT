from functools import cmp_to_key
def sum_digit(n):
    tong=0
    while n>0:
        tong+=n%10
        n//=10
    return tong
def cmp(a,b):
    if sum_digit(a)==sum_digit(b):
        return a-b
    else:
        return sum_digit(a)-sum_digit(b)
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(key=cmp_to_key(cmp))
    for i in a:
        print(i,end=' ')
    print()