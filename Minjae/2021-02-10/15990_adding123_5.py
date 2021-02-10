dp=[[0]*(4) for _ in range(100000+1)]
# dp[i][j]: i를 만드는 경우의수, 마지막으로 더한 숫자가 j
dp[1][1]=1
dp[2][2]=1
dp[3][3]=1
for i in range(100000+1):
    for num in (1, 2, 3):
        for j in (1, 2 ,3):
            if dp[i][j] and num!=j and i+num<=100000:
                dp[i+num][num]+= dp[i][j]
                dp[i+num][num]%=(int(1e9)+9)
for _ in range(int(input())):
    n= int(input())
    print(sum(dp[n])%(int(1e9)+9))


'''
import sys
input=sys.stdin.readline

t=int(input())
nums=[int(input()) for _ in range(t)]

limit=100001
mod=1000000009
dp=[[0,0,0,0] for i in range(limit+1)]

dp[1][1]=1
dp[2][2]=1
dp[3][1]=1
dp[3][2]=1
dp[3][3]=1

for i in range(4,limit+1): # 지금 결정할 i아래론 다 결정됐으니까 갖다 쓰면 되는구나 퇴사같은문제
    dp[i][1]=(dp[i-1][3]+dp[i-1][2])%mod
    dp[i][2]=(dp[i-2][1]+dp[i-2][3])%mod
    dp[i][3]=(dp[i-3][1]+dp[i-3][2])%mod

for num in nums:
    print(sum(dp[num])%mod)
'''