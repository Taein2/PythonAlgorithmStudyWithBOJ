import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())
L= [0]+[*map(int, input().split())]

dp= [0]*(n+1)
# dp[i]: 카드 i장 샀을때 지불할 수 있는 최대 금액
for card in range(1, n+1):
    for i in range(n+1):
        if (i==0 or dp[i]) and i+card<=n:
            dp[i+card]= max(dp[i+card], dp[i]+L[card])

print(dp[n])
