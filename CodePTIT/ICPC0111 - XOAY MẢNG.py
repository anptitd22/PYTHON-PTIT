# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
# Press the green button in the gutter to run the script.
import math
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        for i in range(n):
            print(a[(i+k)%n],end=' ')
        print()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/