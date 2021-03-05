import sys
input = sys.stdin.readline

t = int(input())
mod = 1000000009
dp = [[0] * 1001 for _ in range(1001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1

dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1

for i in range(4,1001):
    for j in range(1,i+1):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 3][j - 1]) % mod

for _ in range(t):
    n,m = map(int,input().split())
    print(dp[n][m])
