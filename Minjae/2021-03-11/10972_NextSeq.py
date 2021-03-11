import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())
L= [*map(int, input().split())]
if L==list(range(n,0,-1)):
    print(-1)
else:
    last=-1
    q=[]
    end=-1
    for i in range(n-1,-1,-1):
        if L[i]>last:
            q.append(L[i])
            last=L[i]
        else:
            end=i
            break
    ths=1e9
    for j in range(end+1,n):
        if L[end]<L[j]:
            ths=min(L[j],ths)
    q.remove(ths)
    q.append(L[i])
    q.sort()
    print(*L[:i], ths, *q)