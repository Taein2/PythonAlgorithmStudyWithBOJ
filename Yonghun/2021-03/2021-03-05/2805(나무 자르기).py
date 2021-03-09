# 이분 탐색
n, m = map(int,input().split())
array = list(map(int,input().split()))

start = 0
end = max(array)

while (start <= end) :
    mid = (start + end) // 2

    sum = 0
    for i in array :
        if i >= mid :
            sum += (i - mid)

    if sum >= m :
        start = mid + 1
    else :
        end = mid - 1
    
print(end)



    