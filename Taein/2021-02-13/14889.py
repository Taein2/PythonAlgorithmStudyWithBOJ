import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
lst = []
for i in range(1,n+1):
    lst.append(i)
team = list(combinations(lst,2))
#다시풀기