import sys; input= lambda: sys.stdin.readline().strip()
n= int(input())
L= [*map(int ,input().split())]
dp=[[0,0] for _ in range(n)]

dp[0]= [L[0], L[0]]
ans=L[0]
for i in range(1,n):
    dp[i][0]= max(dp[i-1][0]+L[i],L[i])
    if i-2>=0:
        dp[i][1]= max(dp[i-1][1]+L[i], dp[i-2][0]+L[i])
    else:
        dp[i][1]= dp[i-1][1]+L[i]

    ans= max(ans, max(dp[i]))

print(ans)