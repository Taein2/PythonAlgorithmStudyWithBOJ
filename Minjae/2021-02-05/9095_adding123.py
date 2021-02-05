t= int(input())
for _ in range(t):
    n= int(input())
    dp=[1]+ [0]*n
    # dp[i]: 숫자 i를 만드는 경우의 수
    for i in range(0,n+1):
        for j in (1, 2, 3):
            if i-j>=0 and dp[i-j]:
                dp[i]+=dp[i-j]
    print(dp[n])