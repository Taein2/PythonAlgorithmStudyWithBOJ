n= int(input())
L=[*map(int, input().split())]

dp=[[1,i] for i in range(n)]

mxdp=1
mxidx=0
for i in range(n):
    for j in range(i):
        if L[j]<L[i]:
            if dp[j][0]+1>dp[i][0]:
                dp[i][0]=dp[j][0]+1
                dp[i][1]=j
                if dp[i][0]>mxdp:
                    mxdp=dp[i][0]
                    mxidx=i
ans=[]                
cur=mxidx
while dp[cur][1]!=cur:
    ans.append(L[cur])
    cur=dp[cur][1]
if not ans or ans[-1]!=L[cur]:
    ans.append(L[cur])

print(mxdp)
print(*reversed(ans))

