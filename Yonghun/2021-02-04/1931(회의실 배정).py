# 회의실 배정
n = int(input())

meeting = [list(map(int,input().split())) for _ in range(n)]
meeting.sort(key = lambda x : (x[1], x[0]))

cnt = 0
end_time = 0
for i, j in meeting :
    if i >= end_time :
        cnt += 1
        end_time = j

print(cnt)

