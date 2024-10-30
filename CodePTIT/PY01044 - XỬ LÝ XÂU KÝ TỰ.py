s,s1,s2=set({}),set({}),set({})
for x in input().split():
    s1.add(x.lower())
for x in input().split():
    s2.add(x.lower())
s3=s1.intersection(s2)
s=s1.union(s2)
a,b=[],[]
for x in s:
    a.append(x)
for x in s3:
    b.append(x)
a.sort()
b.sort()
for x in a:
    print(x,end=' ')
print()
for x in b:
    print(x,end=' ')