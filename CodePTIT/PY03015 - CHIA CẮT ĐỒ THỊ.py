# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
# Press the green button in the gutter to run the script.
import math
from functools import cmp_to_key
from itertools import permutations
check=[False]*101
ke=[[] for _ in range(101)]
def dfs(u):
    check[u]=True
    for i in ke[u]:
        if check[i]==False:
            dfs(i)
if __name__ == '__main__':
    for _ in range(int(input())):
        for i in range(101):
            ke[i].clear()
        check=[False]*101
        n,m=map(int,input().split())
        for _ in range(m):
            x,y=map(int,input().split())
            ke[x].append(y)
            ke[y].append(x)
        cnt=1
        # for i in range(1,n+1):
        #     if check[i]==False:
        #         cnt+=1
        #         dfs(i)
        ans=0
        for i in range(1,n+1):
            check=[False]*101
            check[i]=True
            cnt1=0
            for j in range(1,n+1):
                if check[j]==False:
                    cnt1+=1
                    dfs(j)
            if cnt1>cnt:
                ans=i
                cnt=cnt1
        print(ans)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/