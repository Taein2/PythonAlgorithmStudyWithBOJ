n= int(input())
L= [*map(int, input().split())]
L.sort()
m= int(input())
M= [*map(int, input().split())]
def bs(k):
    lo=0
    hi=n-1
    while lo<hi:
        mid= (lo+hi)//2
        if L[mid]<k:
            lo=mid+1
        elif L[mid]>k:
            hi=mid-1
        else:
            return 1
    if L[lo]==k:
        return 1
    return 0
for el in M:
    print(bs(el),end=' ')