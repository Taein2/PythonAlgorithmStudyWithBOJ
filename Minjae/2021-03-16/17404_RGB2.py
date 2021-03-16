import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())

dp=[[0]*3 for _ in range(n)]

color= [[0]*3 for _ in range(n)]
for i in range(n):
    r, g, b= map(int, input().split())
    color[i][0]=r
    color[i][1]=g
    color[i][2]=b
ans=1e9
# 첫 집 레드
dp[0][0]=color[0][0]
dp[0][1]=1e9
dp[0][2]=1e9
for i in range(1,n):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+color[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+color[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+color[i][2]
ans= min(dp[n-1][1], dp[n-1][2])


# 첫 집 그린
dp[0][0]=1e9
dp[0][1]=color[0][1]
dp[0][2]=1e9
for i in range(1,n):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+color[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+color[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+color[i][2]

ans= min(ans, dp[n-1][0], dp[n-1][2])

# 첫 집 그린
dp[0][0]=1e9
dp[0][1]=1e9
dp[0][2]=color[0][2]
for i in range(1,n):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+color[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+color[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+color[i][2]

ans= min(ans, dp[n-1][0], dp[n-1][1])

print(ans)