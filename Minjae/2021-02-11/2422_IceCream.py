n, m= map(int, input().split())
edge= [[] for i in range(n+1)]
for _ in range(m):
    a, b= map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
ans=0
chk=[0]*(n+1)
def backtracking(i, cnt): # 순도 100% 백트래킹. 이 짓을 할 이유가 없었다
    global ans
    if cnt+n-(i-1)<3:
        return
    if i>n:
        return
    if chk[i]>0:
        backtracking(i+1,cnt)
        return

    #print(i, end=' ')
    chk[i]+=1 
    cnt+=1
    if cnt==3:
        ans+=1
    for v2 in edge[i]:
        chk[v2]+=1
    #print(chk)
    if cnt<3:
        backtracking(i+1, cnt)
     
    for v2 in edge[i]:
        chk[v2]-=1
    chk[i]-=1
    #print()
    backtracking(i+1, cnt-1)

backtracking(1, 0)
print(ans)