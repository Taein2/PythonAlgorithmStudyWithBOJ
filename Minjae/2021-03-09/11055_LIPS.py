n= int(input())
L=[*map(int, input().split())]
dp=[0]*n
for i in range(n):
    dp[i]=L[i]
    for j in range(i):
        if L[j]<L[i]:
            dp[i]=max(dp[i], dp[j]+L[i])
print(max(dp))