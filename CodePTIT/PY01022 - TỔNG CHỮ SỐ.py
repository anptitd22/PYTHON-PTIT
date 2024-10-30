def Try(n):
    if len(n)==1: return 0
    n=[ord(x)-48 for x in n]
    return 1+ Try(str(sum(n)))
print(Try(input()))