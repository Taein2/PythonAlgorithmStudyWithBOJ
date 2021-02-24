import sys
input = sys.stdin.readline
lst = [list(map(str,input().split())) for _ in range(5)]
result = []
def dfs(x,y,num):
    if len(num) == 6:
        if num not in result:
            result.append(num)
        return
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]
        if ddx >= 0 and ddx < 5 and ddy >= 0 and ddy <5:
            dfs(ddx,ddy,num+lst[ddx][ddy])

for i in range(5):
    for j in range(5):
        dfs(i,j,lst[i][j])
print(len(result))