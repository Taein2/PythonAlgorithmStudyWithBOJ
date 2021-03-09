# 기타 레슨, 이분 탐색

n, m = map(int,input().split())
lesson = list(map(int,input().split()))
 
start = max(lesson) # 레슨 값 중 최댓값을 포함해야함.
end = sum(lesson)  # 하나의 블루레이에 담은 경우

while start <= end :
    mid = (start + end) // 2

    cnt = 0 # 블루레이 개수
    time = 0 # 레슨 시간의 합

    for i in lesson :
        if time + i > mid : # m 보다 레슨 값의 합이 커지면 새로운 블루레이
            cnt += 1
            time = 0
        
        time += i
    
    if time != 0 :
        cnt += 1
    
    if cnt <= m : # 블루레이 개수가 모자르면 크기를 줄여서 개수 늘림
        end = mid - 1 
    else : # 블루레이 개수가 초과하면 크기를 늘려서 개수 줄임
        start = mid + 1 

print(start)
