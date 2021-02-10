T = int(input())
D = [[0] * 4 for _ in range(100001)]

# dp[i][j] : i를 만드는 데 더해지는 끝 수가 j인 경우의 수
D[1][1] = 1
D[2][2] = 1
D[3][1] = 1
D[3][2] = 1
D[3][3] = 1

for i in range(4, 100001):
    for j in [1, 2, 3]: # 맨 끝에 더해지는 수는 1, 2, 3
        D[i][j] = ((D[i - j][1] + D[i -j][2] + D[i - j][3]) - D[i - j][j]) % 1000000009

for _ in range(T):
    n = int(input())
    print((D[n][1] + D[n][2] + D[n][3]) % 1000000009)
    