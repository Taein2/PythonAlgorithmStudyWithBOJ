n= int(input())
L= [*map(int, input().split())]
# dp[i]: i 번째로 끝나는 최장증가수열길이
dp=[1]*n
for i in range(n):
    for j in range(i-1,-1,-1):
        if L[j]<L[i]:
            dp[i]= max(dp[i],dp[j]+1)
print(max(dp))