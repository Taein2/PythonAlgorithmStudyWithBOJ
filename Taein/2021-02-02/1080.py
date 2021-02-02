import sys

input = sys.stdin.readline

N, M = map(int,input().split())

arr = [list(map(int,input().strip())) for _ in range(N)]
result = [list(map(int,input().strip())) for _ in range(N)]

def solve(i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            arr[x][y] = 1-arr[x][y]

count = 0
for i in range(N-2):
    for j in range(M-2):
        if arr[i][j] != result[i][j]:
            count += 1
            solve(i,j) 
check = True
for i in range(N):
    for j in range(M):
        if arr[i][j] != result[i][j]:
            check = False

if check:
    print(count) 
else:
    print(-1)