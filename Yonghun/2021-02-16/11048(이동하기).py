n, m = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]
D = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1) :
    for j in range(1, m + 1) :
        D[i][j] = array[i-1][j-1] + max(D[i-1][j], D[i][j-1], D[i-1][j-1])


print(D[n][m]) 