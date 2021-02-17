import sys
input = sys.stdin.readline

n = int(input())
dp = [0,1]
if n == 0 :
    print(0)
elif n==1:
    print(1)
else:
    for i in range(2,n+1):
        dp.append(dp[i-2]+dp[i-1])
    print(dp[n])