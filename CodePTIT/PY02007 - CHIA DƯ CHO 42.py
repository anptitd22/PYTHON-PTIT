from sys import stdin
a=[]
for s in stdin:       
    a+=list(map(int,s.split()))
s=set([x%42 for x in a])
print(len(s))