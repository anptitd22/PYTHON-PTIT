n,m=map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=a.intersection(b)
d=a.difference(b)
e=b.difference(a)
for x in sorted(list(c)):
    print(x,end=' ')
print()
for x in sorted(list(d)):
    print(x,end=' ')
print()
for x in sorted(list(e)):
    print(x,end=' ')
print()