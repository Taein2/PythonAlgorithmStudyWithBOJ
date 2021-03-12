n= int(input())
dp=[0]*(max(6,n+1))
dp[1]=1
dp[2]=2
dp[3]=3
dp[4]=4
dp[5]=5
for i in range(6,n+1):
    dp[i]= max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)
print(dp[n])