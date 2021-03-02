n, s, m= map(int, input().split())
dp=[[False]*(m+1) for _ in range(n+1)]
#dp[i][j]: i번째 연주를 위해 설정할 수 있는 볼륨 이면 True
vol= [0]+[*map(int, input().split())]
dp[0][s]=True
for i in range(1,n+1):
    for j in range(m+1):
        if dp[i-1][j] and j-vol[i]>=0:
            dp[i][j-vol[i]]=True
    for j in range(m,-1,-1):
        if dp[i-1][j] and j+vol[i]<=m:
            dp[i][j+vol[i]]=True
for j in range(m,-1,-1):
    if dp[n][j]:
        print(j)
        exit()
print(-1)