import sys
input = sys.stdin.readline

t = int(input())
mod = 1000000009
dp = [1]*1000001
dp[2] = 2
result = []
for i in range(3,len(dp)):
    dp[i] = dp[i-1]%mod + dp[i-2]%mod + dp[i-3]%mod

for i in range(t):
    n = int(input())
    print(dp[n]%mod)
    