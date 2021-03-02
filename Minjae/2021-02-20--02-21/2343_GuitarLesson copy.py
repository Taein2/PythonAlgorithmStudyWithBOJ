#WA
n, m= map(int, input().split())
L=[*map(int, input().split())]

mx= 100000*10000


def record(blueray):
    cnt=1
    k=blueray
    for el in L:
        if el<=k:
            k-=el
        else:
            cnt+=1
            k=blueray-el
    return cnt

lo=0
hi=mx
while lo<hi:
    mid= (lo+hi)//2
    if record(mid)<m:
        hi= mid-1
    elif record(mid)>m:
        lo= mid+1
    else:
        hi=mid

if record(lo)==m:
    print(lo)
else:
    print(hi)