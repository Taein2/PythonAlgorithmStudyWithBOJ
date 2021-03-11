#WA 
n= int(input())
dp= [[[0]*2 for _ in range(4)] for _ in range(n)]

dp[0][0]= [1,0]
dp[0][1]= [0,0]
dp[0][2]= [0,0] # [dp[i-1][1][0],sum(dp[i-1][1])]
dp[0][3]= [1,0]
'''
tmp= max([dp[i-1][k][1] for k in range(4)]
[max(dp[i-1][0][0], dp[i-1][2])+tmp, tmp]
'''


for i in range(1,n):
    a,b= sorted(dp[i-1])[-1]

    dp[i][0]= [a+1,b]
    dp[i][1]= [a,b]
    dp[i][2]= [dp[i-1][1][0],dp[i-1][1][0]]
    c, d= 0, 0
    for j in range(4):
        #print(dp[i-1][j])
        if sum(dp[i-1][j])==c+d:
            if d<dp[i-1][j][1]:
                c,d= dp[i-1][j]
        elif sum(dp[i-1][j])>c+d:
                c,d= dp[i-1][j]
    dp[i][3]= [c+d,d]
    #print(dp[i])

print(max([dp[n-1][k][0] for k in range(4)]))