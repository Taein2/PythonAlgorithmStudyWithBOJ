from collections import deque
n, k= map(int, input().split())
L=deque()
for i in range(1,n+1):
    L.append(i)

ans=[]
while L:
    for _ in range(k-1):
        q= L.popleft()
        L.append(q)
    q= L.popleft()
    ans.append(str(q))

print('<',end='')
print(', '.join(ans),end='')
print('>',end='')