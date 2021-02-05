n= int(input())

dp=[0, 0]+ [1e9]*(n+1)
for i in range(2, n+1):
    if not i%3:
        dp[i]= min(dp[i//3]+1, dp[i])
    if not i%2:
        dp[i]= min(dp[i//2]+1, dp[i])
    dp[i]= min(dp[i], dp[i-1]+1)
    #print(f'dp[{i}]: {dp[i]}')

print(dp[n])