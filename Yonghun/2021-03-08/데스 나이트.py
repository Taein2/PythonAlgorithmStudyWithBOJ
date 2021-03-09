from collections import deque
import sys
input = sys.stdin.readline

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

n = int(input())
r1,c1, r2,c2 = map(int,input().split())
chk = [[0] * n for _ in range(n)]
 
def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
    
        if x == r2 and y == c2:
            return chk[x][y]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if chk[nx][ny] == 0:
                    chk[nx][ny] = chk[x][y] + 1
                    q.append([nx, ny])
                    
    return -1

res = bfs(r1, c1)
print(res)