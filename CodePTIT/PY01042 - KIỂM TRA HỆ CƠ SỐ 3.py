# def check(n):
#     for x in n:
#         if x not in '012':
#             return False
#     return True
# t=int(input())
# for test in range(t):
#     a=list(input())
#     if check(a):
#         print("YES")
#     else: 
#         print("NO")
t=int(input())
for test in range(t):
    a=list(input())
    b=[x for x in a if x in '012']
    if len(b)==len(a):
        print("YES")
    else:
        print("NO")