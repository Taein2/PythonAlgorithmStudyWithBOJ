n= int(input())
L= [0]+ [tuple(map(int, input().split())) for _ in range(n)]

dp=[0]*(n+1)
#dp[i]:i날을 끝으로 상담 끝낼때 낼 수 있는 최대 수익
for i in range(1,n+1):
    if i+L[i][0]-1<=n:
        dp[i+L[i][0]-1]= max(dp[i+L[i][0]-1], dp[i-1]+L[i][1])
        # dp[i] 이 완성 돼 있다. 끌고 가야 하는 이유? 하루 이상 건너뛴 게 최대일 수 있기때문
    dp[i]= max(dp[i], dp[i-1])
print(dp[n])
