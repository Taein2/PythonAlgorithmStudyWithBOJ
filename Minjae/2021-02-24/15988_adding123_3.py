M= int(1e6)
dp=[1]+[0]*M

for i in range(M+1):
    for num in (1,2,3):
        if dp[i] and i+num<=M:
            dp[i+num]=(dp[i+num]+dp[i])%(int(1e9)+9)
for _ in range(int(input())):
    print(dp[int(input())])