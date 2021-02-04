import sys; input= lambda:sys.stdin.readline().rstrip()
from functools import cmp_to_key as cmp
n= int(input())
sch=[]
for _ in range(n):
    a, b= map(int, input().split())
    sch.append((a, b))

sch.sort(key= cmp(lambda a, b: a[0]-b[0] if a[1]==b[1] else a[1]-b[1]))

end=0
cnt=0
for st, ed in sch:
    if end<=st:
        cnt+=1
        end=ed

print(cnt)
