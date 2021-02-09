dp=[1]+[0]*10000
for num in (1,2,3):
    for i in range(10001):
        if dp[i] and i+num<=10000:
            dp[i+num]+=dp[i]
for _ in range(int(input())):
    print(dp[int(input())])
