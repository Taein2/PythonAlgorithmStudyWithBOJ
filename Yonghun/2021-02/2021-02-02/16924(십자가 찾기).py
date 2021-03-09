# 시뮬레이션 & 구현
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n,m = map(int,input().split())
array = [list(input()) for _ in range(n)]
answer = []
check = [[0] * m for _ in range(n)]

for x in range(n):
    for y in range(m):
        if array[x][y] == '*': # x,y를 십자가의 중심으로 두고 탐색.
            cross_length = 1
            while True:
                Flag = True
                for k in range(4):
                    nx = x + dx[k] * cross_length
                    ny = y + dy[k] * cross_length
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or array[nx][ny] == '.':
                        Flag = False

                if not Flag :
                    break

                check[x][y] = True

                for k in range(4):
                    nx = x + dx[k] * cross_length
                    ny = y + dy[k] * cross_length
                    check[nx][ny]  = True

                answer.append((x + 1, y + 1, cross_length))
                cross_length += 1

if len(answer) == 0 : # 십자가가 없다.
    print(-1)
    exit()

for i in range(n):
    for j in range(m):
        if array[i][j] == '*' and check[i][j] == False:
            print(-1)
            exit()

print(len(answer))
for cross in answer:
    print(cross[0], cross[1], cross[2])