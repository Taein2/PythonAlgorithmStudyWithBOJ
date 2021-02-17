n= int(input())
L= [*map(int, input().split())]
dp=[0]+[1e9]*(n-1)
for i in range(n):
    for j in range(1,min(i+L[i]+1,n)):
        dp[j]=min(dp[j], dp[i]+1) 
print([dp[n-1],-1][dp[n-1]==1e9])