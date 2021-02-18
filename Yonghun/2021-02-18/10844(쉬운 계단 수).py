n = int(input())
dp = [[1] * 10 for _ in range(n + 1)]
# dp[i][j] 에서 i은 자리수, j는 수의 마지막 숫자
# 1자리 수는 0이 끝에 올 수 없으므로 0개로 저장

dp[1][0] = 0
if n != 1 :
    for i in range(2, n + 1):
        for j in range(0, 10):
            if j==0 :
                dp[i][j] = dp[i-1][1]
            elif j==9 :
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n]) % 1000000000)