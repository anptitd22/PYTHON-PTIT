import math
def nto(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return n>1
def check(n):
    for i in range(len(a)):
        if nto(a[i]) and nto(a[len(a)-1]-a[i]):
            return i
    return "NOT FOUND"
n=int(input())
a=[]
st=set({})
for i in map(int,input().split()):
    if not i in st:
        a.append(i)
        if len(a)>1:
            a[len(a)-1]+=a[len(a)-2]
    st.add(i)
print(check(a))