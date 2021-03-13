from collections import deque
# 숨바꼭질

n, k = map(int,input().split()) # 수빈이의 현재 위치, 동생의 위치
time = [-1 for _ in range(100001)] # 방문 체크
time[n] = 0 # 시작점 체크

q = deque()
q.append(n)

# bfs 탐색
while q : 
    n = q.popleft()

    if n == k :
        break

    for nx in [(n - 1), (n + 1), (2 * n)] :
        if 0 <= nx < 100001 and time[nx] == -1 :
            time[nx] = time[n] + 1
            q.append(nx)

print(time[k])