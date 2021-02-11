n= int(input())
L= [0]+ [tuple(map(int, input().split())) for _ in range(n)] + [(0,0)]

dp= [0]*(n+2)
# dp[i]: i날전날 이하로 상담마쳤을때 받을 수 있는 최대 금액

for i in range(1, n+2):
    dp[i]= max(dp[i], dp[i-1]) # 이 디피가 완성된 후에 써야하니까 이걸 앞에 놔야한다.
    if i+L[i][0]<=n+1:
        dp[i+L[i][0]]= max(dp[i+L[i][0]], dp[i]+L[i][1])
print(dp[n+1])