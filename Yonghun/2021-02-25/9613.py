from math import gcd
from itertools import combinations as cb

T = int(input())

for i in range(T) :
    array = list(map(int,input().split()))
    array = array[1 :]
    combi = list(cb(array, 2))
    ans = 0
    for a, b in combi :
        ans += gcd(a, b)

    print(ans)

