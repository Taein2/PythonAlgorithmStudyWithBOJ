# dp[i][0] 위나 아래 하나
# dp[i][1] 위두개나 아래 둘
# dp[i][2] 풀
n= int(input())
dp= [[0]*3 for _ in range(max(n,2)+1)]
dp[1][0]=0
dp[1][1]=2
dp[1][2]=0

dp[2][0]=2
dp[2][1]=0
dp[2][2]=3

for i in range(3,n+1):
    dp[i][0]= dp[i-1][1]
    dp[i][1]=dp[i-1][2]*2+dp[i-1][0]
    dp[i][2]=dp[i-2][2]+dp[i][0]
print(dp[n][2])


'''
0
17
0
93
0
507
'''