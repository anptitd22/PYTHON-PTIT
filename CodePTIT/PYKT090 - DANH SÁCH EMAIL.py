f=open("CONTACT.in","r")
s=set()
lines=f.readlines()
for x in lines:
    s.add(x.strip().lower())
s=sorted(s)
for x in s:
    print(x)