import sys
import heapq
input = sys.stdin.readline

n = int(input())
p,d = [],[]
k = [list(map(int,input().split())) for _ in range(n)]
k.sort(key=lambda x:x[1])
result = []
for i in k:
    heapq.heappush(result,i[0])
    if len(result) > i[1]:
        heapq.heappop(result)
print(sum(result))
