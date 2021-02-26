n = int(input())
D = [[0] * 10 for _ in range(1001)]

for j in range(10):
    D[1][j] = 1

for i in range(2, n + 1):
    for j in range(10):
        for col in range(j + 1):
            D[i][j] += D[i - 1][col]

print(sum(D[n]) % 10007)


# 맨 앞자리 수가 0이면 다음 숫자로 0~9까지 다 올 수 있으므로 dp[i][0] = dp[i-1][0] + dp[i-1][1] + ... + dp[i-1][8] + dp[i-1][9]
# 맨 앞자리 수가 1이면  다음 숫자로 1~9까지 올 수 있으므로 dp[i][1] = dp[i-1][0] + dp[i-1][1] + ... + dp[i-1][8] + dp[i-1][9]

# 따라서 dp[i][j] += dp[i-1][k] (k -> j to 10)가 성립한다. 
