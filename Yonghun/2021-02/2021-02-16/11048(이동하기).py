n, m = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]
D = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(0, n) :
    for j in range(0, m) :
        D[i][j] = max(D[i-1][j], D[i][j-1])
        D[i][j] += array[i][j]

print(D[n-1][m-1])
