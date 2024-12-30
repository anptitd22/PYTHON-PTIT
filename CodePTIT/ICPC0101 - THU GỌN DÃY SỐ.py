# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a=[]
    n=int(input())
    b=list(map(int,input().split()))
    for i in range(n):
        if len(a)==0:
            a.append(b[i])
        else:
            if (a[len(a)-1]+b[i])%2==0:
                a.pop()
            else:
                a.append(b[i])
    print(len(a))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/