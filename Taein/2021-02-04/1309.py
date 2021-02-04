import sys
input = sys.stdin.readline
N = int(input())
dp = [1 for _ in range(N+1)]
dp[1] = 3
if N == 1:
    print(dp[1])
else:
    for i in range(2,N+1):
        dp[i] = (dp[i-2] + dp[i-1] * 2) % 9901
    print(dp[N])