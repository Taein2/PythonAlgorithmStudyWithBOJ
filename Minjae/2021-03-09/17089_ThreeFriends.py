import sys; input= lambda: sys.stdin.readline().rstrip();r=range
n, m= map(int, input().split())
edge= [[] for _ in r(n+1)]

deg= [0]*(n+1)

for _ in r(m):
    a, b= map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
    deg[a]+=1
    deg[b]+=1

Trys=[]
def friend(v):
    for v2 in edge[v]:
        if deg[v2]<2 or v2<=v:
            continue
        for v3 in edge[v2]:
            if deg[v3]<2 or v3<=v2:
                continue
            for v4 in edge[v3]:
                if v4==v:
                    Trys.append((v,v2,v3))
                

for i in r(1,n+1):
    if deg[i]>=2:
        friend(i)

mn=1e9
for a, b, c in Trys:
    cnt=0
    for v2 in edge[a]:
        if v2!=b and v2!=c:
            cnt+=1
    for v2 in edge[b]:
        if v2!=a and v2!=c:
            cnt+=1
    for v2 in edge[c]:
        if v2!=a and v2!=b:
            cnt+=1
    mn= min(cnt, mn)

print([mn,-1][mn==1e9])