import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*101
dp[0] = 1
dp[1] = 2
dp[2] = 3
for i in range(3,n):
    dp[i] = dp[i-1] +1
    for j in range(i-3,-1,-1):
        dp[i] = max(dp[i], dp[j] * (i - j - 1))
print(dp[n-1])
