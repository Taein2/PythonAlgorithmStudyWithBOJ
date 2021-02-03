n= int(input())
#dp[i][j]: 숫자 i를 나타내는 문자를 j개 써서 만드는 경우의 수
#구해야할 답: 문자를 j개 써서 만들 수 있는 숫자의 개수
dp=[[0]+[0]*n for _ in range(1001+50)]

for char in (1, 5, 10, 50):
    dp[char][1]=1
    for i in range(1001):
            for j in range(n):
                if dp[i][j]:
                    dp[i+char][j+1]+=1
print(len([i for i in range(1001) if dp[i][n]]))
