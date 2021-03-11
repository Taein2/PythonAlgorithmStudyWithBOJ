#dp[i][j]: 숫자i를 만드는 데 숫자 j개 쓰는 경우의 수
E= int(1e9)+9
n=1000
m=n
dp= [[0]+[0]*m for _ in range(n+1)]

dp[1][1]=1
dp[2][1]=1
dp[3][1]=1

for i in range(1,n+1):
    for k in range(m):
        for j in (1,2,3):
            if i-j>=0:
                dp[i][k+1]=(dp[i][k+1]+ dp[i-j][k])%E

for _ in range(int(input())):
    a, b= map(int, input().split())

    print(dp[a][b])