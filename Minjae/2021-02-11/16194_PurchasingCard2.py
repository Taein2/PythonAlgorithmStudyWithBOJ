n= int(input())
L =[0]+ [*map(int, input().split())]

dp=[0]+ [1e9]*n
for card in range(1,n+1):
    for i in range(1,n+1): # ** range 설정을 애초에 card부터로 놨다면 if 문이 필요 없다.
        if i-card>=0:
            dp[i]= min(dp[i], dp[i-card]+L[card])
print(dp[n])