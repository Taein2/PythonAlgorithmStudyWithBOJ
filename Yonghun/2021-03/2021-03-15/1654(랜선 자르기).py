# 랜선 자르기

k, n = map(int,input().split()) # 현재 보유한 랜선의 개수, 필요한 랜선의 개수
array = []
for _ in range(k) :
    array.append(int(input()))

array.sort()

start = 1
end = array[-1]

while (start <= end) :
    mid = (start + end) // 2 
    
    total = 0

    for i in array :
        total += (i // mid)
        
    if total < n :
        end = mid - 1
    else :
        start = mid + 1

print(end)