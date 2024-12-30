def rotate(s):
    tong=sum([ord(x)-ord('A') for x in s])
    tmp=""
    for x in s:
        t=(ord(x)-65+tong)%26
        tmp+=str(chr(t+65))
    return tmp
def merge(s1,s2):
    tmp=""
    for i in range(len(s1)):
        t=(ord(s1[i])-65+(ord(s2[i])-ord('A')))%26
        tmp+=chr(t+65)
    return tmp
if __name__ == '__main__':
    for _ in range(int(input())):
        s=input()
        a=rotate(s[:len(s)//2:])
        b=rotate(s[len(s)//2::])
        a=merge(a,b)
        print(a)