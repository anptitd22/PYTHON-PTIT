def he10(n,b):
    ans=0
    for i in n:
        ans=ans*b+int(i)
    return ans
def heb(n,b):
    if n==0: return 
    heb(n//b,b)
    if n%b>9:
        print(chr(65+(n%b)%10),end='')
    else:
        print(n%b,end='')
for t in range(int(input())):
    b=int(input())
    n=input()
    heb(he10(n,2),b)
    print()