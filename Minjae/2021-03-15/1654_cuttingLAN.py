import sys; input= lambda: sys.stdin.readline().rstrip()
k, n= map(int, input().split())

LANs=[]
for el in range(k):
    LANs.append(int(input()))

def cut(k):
    sm=0
    for el in LANs:
        sm+=el//k
    return sm
lo=1
hi=int(1e10) #2^31>1e9
while lo+1<hi:
    mid= (lo+hi)//2
    if n<=cut(mid):
        lo=mid
    else:
        hi=mid-1
if n<=cut(hi):
    print(hi)
else:
    print(lo) 