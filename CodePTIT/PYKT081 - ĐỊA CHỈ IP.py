def check(n):
    m=n.count(".")
    if len(n) >15: return False
    if m!=3: return False
    a=n.split(".")
    for x in a:
        if x.isdigit():
            if int(x)<0 or int(x)>255:
                return False
        else:
            return False
    return True
for t in range(int(input())):
    n=input()
    if check(n):
        print("YES")
    else:
        print("NO")