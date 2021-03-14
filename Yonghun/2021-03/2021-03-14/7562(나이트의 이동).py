from collections import deque
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y, end_x, end_y) :
    q = deque()
    q.append((x, y))
    while q :
        x, y = q.popleft()

        if x == end_x and y == end_y :
            return array[x][y]
        
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if array[nx][ny] == -1 :
                    array[nx][ny] = array[x][y] + 1
                    q.append([nx, ny])

    return -1

T = int(input())
for _ in range(T) :

    n = int(input())
    array = [[-1] * (n + 1) for _ in range(n + 1)]

    x, y = map(int,input().split())
    array[x][y] = 0

    end_x, end_y = map(int,input().split())
    print(bfs(x, y, end_x, end_y))


