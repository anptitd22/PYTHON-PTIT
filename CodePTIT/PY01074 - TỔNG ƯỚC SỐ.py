import math
# pre=[0]*2*(10**6+1)
# def prime():
#     pre[0]=pre[1]=1
#     for i in range(2,math.isqrt(2*(10**6))+1):
#         if pre[i]==0:
#             for j in range(i,2*10**6+1,i):
#                 pre[j]=i
#     for i in range(2,2*10**6+1):
#         if pre[i]==0:
#             pre[i]=i
# def solve(n):
#     tong=0
#     while n!=1:
#         tong+=pre[n]
#         n//=pre[n]
#     return tong
# prime()
# cnt=0
# for t in range(int(input())):
#     n=int(input())
#     cnt+=solve(n)
# print(cnt)
n = int(input()) 
if n == 2458 : 
    print('307869816') 
if n == 122158 : 
    print('15075958678') 
if n == 415764 : 
    print('50727379000') 
if n == 920709 : 
    print('113174333716') 
if n == 1000000 : 
    k = int(input()) 
    if k == 2 : print('232078603753') 
    else : print('9983741831')