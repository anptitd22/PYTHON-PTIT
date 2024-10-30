def check(n):
    if n.count("888")>0:
        return "NO"
    else:
       for i in n:
           if i!='6' and i !='8':
               return"NO"
    return "YES" 
n=input()
print(check(n))