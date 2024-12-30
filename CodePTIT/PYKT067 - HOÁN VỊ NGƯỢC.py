# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
# Press the green button in the gutter to run the script.
import math
from functools import cmp_to_key
from itertools import permutations
if __name__ == '__main__':
    for _ in range(int(input())):
        n=int(input())
        a=list(permutations([str(x) for x in range(1,n+1)]))
        a.reverse()
        print(len(a))
        for i in a:
            print(''.join(i),end=' ')
        print()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/