# 순회강연
import heapq
n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]
array.sort(key = lambda x : x[1]) # 데드라인을 기준으로 오름차순 정렬.

p_list = []

for num in array :
    heapq.heappush(p_list, num[0])
    if len(p_list) > num[1] :
        heapq.heappop(p_list)

print(sum(p_list))
# p값이 담긴 목록이 몇일안에 해야하는 마감 일을 넘긴 경우 가장 작은 값을 제거해준다.