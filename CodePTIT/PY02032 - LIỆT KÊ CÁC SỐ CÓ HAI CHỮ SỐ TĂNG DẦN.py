n=input()
st=set({})
if len(n)%2==1:
    n=n[:len(n)-1]
for i in range(0,len(n),2):
    st.add(n[i:i+2])
b=sorted(list(st))
for x in b:
    print(x,end=' ')
print()