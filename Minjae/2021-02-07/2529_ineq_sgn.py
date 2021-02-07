k= int(input())+1
L=input().split()
indegree= [0]*(k+1)
ind=[]
edge=[[] for _ in range(k+1)]
for idx,a in enumerate(L):
    if a=='<':
        edge[idx+1].append(idx)
        indegree[idx]+=1
    else:
        edge[idx].append(idx+1)
        indegree[idx+1]+=1
ind=indegree[::]
num=list(range(10-k,10))
ans=[0]*(k)
chk=[False]*k

def dfsSP(v):
    if chk[v]: return
    ans[v]=num.pop()
    chk[v]=True
    for v2 in edge[v]:
        indegree[v2]-=1
        if not indegree[v2]:
            dfsSP(v2)


for i in range(k):
    if indegree[i]==0:
        dfsSP(i)

[print(el,end='') for el in ans]
print()

num=list(range(k))
ans=[0]*(k)
chk=[False]*k

def dfsminSP(v):
    if chk[v]: return
    ans[v]=num.pop()
    chk[v]=True
    for v2 in edge[v][::-1]:
        ind[v2]-=1
        if not ind[v2]:
            dfsminSP(v2)


for i in range(k-1,-1,-1):
    if ind[i]==0:
        dfsminSP(i)

[print(el,end='') for el in ans]

