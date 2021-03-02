n= int(input())
e= int(input())

def find(v):
    if v== par[v]: # if parent
        return v

    par[v]=find(par[v])
    return par[v]

def union(a,b):
    a= find(a)
    b= find(b)
    if a<b:
        par[b]=a
    else:
        par[a]=b
par= list(range(n+1))
for _ in range(e):
    a, b=map(int, input().split())
    union(a,b)

ans=0
for i in range(1,n+1):
    find(i)
    
for i in range(2,n+1):
    if par[i]==1:
        ans+=1
print(ans)