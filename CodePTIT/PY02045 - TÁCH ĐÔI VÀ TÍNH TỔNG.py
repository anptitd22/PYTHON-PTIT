def tong(n):
    if len(n)==1:
        return
    res=int(n[:len(n)//2])+int(n[len(n)//2:])
    print(res)
    tong(str(res))
tong(input())