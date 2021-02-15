import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

p = list(permutations(arr,n))

result = 0
for i in p:
    s = 0
    li = list(i)
    for j in range(1,n):
        s += abs(li[j]-li[j-1])
    result = max(result,s)
print(result)
