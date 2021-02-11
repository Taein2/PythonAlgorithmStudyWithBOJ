
n= int(input())
dp= [0]*(100000)

dic= {}
for i in range(1000):
    if i**2<=100000:
        dic[i**2]=1

dp= [0]+ [1e9]*(n+1)
for k in dic.keys():
    for i in range(n+1):
        if i + k<= n:
            dp[i+k]= min(dp[i+k], dp[i]+1)

print(dp[n])
