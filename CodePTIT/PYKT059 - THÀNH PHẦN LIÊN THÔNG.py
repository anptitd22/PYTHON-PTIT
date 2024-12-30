# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
# Press the green button in the gutter to run the script.
import math
from functools import cmp_to_key
check = [False]*301
ke = [[] for _ in range (301)]
def dfs(u):
    check[u]=True
    for i in ke[u]:
        if check[i] == False:
            dfs(i)
if __name__ == '__main__':
    n,m,x=map(int,input().split())
    for i in range(m):
        y,z=map(int,input().split())
        ke[z].append(y)
        ke[y].append(z)
    dfs(x)
    for i in range(1,n+1):
        if check[i] == False:
            print(i)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/