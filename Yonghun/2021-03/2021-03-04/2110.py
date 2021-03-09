# 이분탐색
import sys
n, c = map(int,input().split()) # 집의 개수, 공유기의 개수

array = [int(sys.stdin.readline()) for _ in range(n)]
array.sort()

result = 0
start = 1 # 최소 거리
end =  array[-1] - array[0] # 최대 거리

# 가장 인접한 두 공유기 사이의 거리를 최대로 만들기.
while (start <= end) :
    mid = (start + end) // 2 # 인접한 공유기 사이의 거리인 gap
    value = array[0]
    count = 1 # 공유기 개수
    
    for i in range(1, n) :
        if array[i] >= (value + mid) : # gap과 value를 더한 값보다 array[i] 가 크면 설치 가능, 더 멀리 있다는 뜻으로
            value = array[i]
            count += 1 # 공유기 설치

    if count < c : # c개 만큼 설치할 수 없으면 gap을 감소시킨다.
        end = mid - 1
    else : # c개 이상의 공 유기를 설치할 수 있는 경우, gap를 증가시켜본다.
        start = mid + 1
        result = mid
        
print(result)