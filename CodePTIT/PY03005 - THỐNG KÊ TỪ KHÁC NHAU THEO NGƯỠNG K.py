import re
import sys
from functools import cmp_to_key
d={}
def cmp(a,b):
    if d[a]==d[b]:
        if a>b:
            return 1
        else:
            return -1
    else:
        return d[b]-d[a]
doc=''
# input=sys.stdin.read()
n,k=map(int,input().split())
for _ in range(n):
    res=re.split('[^a-z0-9]',input().lower())
    for x in res:
        if len(x)==0: continue
        if x in d:
            d[x]+=1
        else:
            d[x]=1
ans = sorted(d,key=cmp_to_key(cmp))
for x in ans:
    if d[x]>=k:
        print(x,d[x])