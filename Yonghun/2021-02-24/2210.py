dx = [1,0,-1,0]
dy = [0,1,0,-1]
array = [list(map(int,input().split())) for _ in range(5)]

answer = set()
def solve(x, y, cnt, s) :
    s += str(array[x][y])
    cnt += 1

    if cnt == 6 :
        answer.add(s)
        return
    
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 :
            solve(nx, ny, cnt , s)
    

for i in range(5) :
    for j in range(5) :
        solve(i,j,0,"")

print(len(answer))