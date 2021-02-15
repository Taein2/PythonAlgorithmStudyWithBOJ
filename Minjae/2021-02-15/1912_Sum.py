n= int(input())
L= [*map(int, input().split())]
dp= [0]*n

for i in range(n):
    dp[i]= max(dp[max(i-1,0)]+L[i], L[i])
print(max(dp))