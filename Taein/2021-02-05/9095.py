import sys
input = sys.stdin.readline

T = int(input())
dp = [1 for _ in range(11)]
dp[2] = 2
dp[3] = 4

for _ in range(T):
    N = int(input())
    for i in range(4,N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[N])