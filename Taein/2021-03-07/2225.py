import sys
input = sys.stdin.readline

n,k = map(int,input().split())
mod = 1000000000
dp = [1]
dp += [0]*n
for i in range(1,k+1):
    for j in range(1,n+1):
        dp[j] = (dp[j] + dp [j-1]) % mod
print(dp[n])
