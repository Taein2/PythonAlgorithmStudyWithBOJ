from functools import cmp_to_key as cmp
import sys; input= lambda: sys.stdin.readline().strip()
s=input()
L=[]
for idx, el in enumerate(s):
    L.append([idx,ord(el)])

def f(a, b):
    x=a
    y=b

    while x[1]==y[1]:
        if x[0]+1==len(s):
            return -1
        elif y[0]+1==len(s):
            return 1
        x=(x[0]+1, ord(s[x[0]+1]))
        y=(y[0]+1, ord(s[y[0]+1]))
    return x[1]-y[1]


L.sort(key= cmp(f))

for el in L:
    print(s[el[0]:])