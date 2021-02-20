# 순회강연
import heapq
n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]
array.sort(key = lambda x : x[1]) # 데드라인을 기준으로 정렬.

sums = []
for num in array :
    heapq.heappush(sums, num[0])
    if len(sums) > num[1] :
        heapq.heappop(sums)

print(sum(sums))