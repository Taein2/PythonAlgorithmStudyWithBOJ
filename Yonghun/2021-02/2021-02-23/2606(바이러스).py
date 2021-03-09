# BFS
from collections import deque

n = int(input())
m = int(input())
array = [[] for _ in range(n + 1)]

for _ in range(m) :
    a, b = map(int,input().split())
    array[a].append(b)
    array[b].append(a)

def bfs() :
    q = deque([1])
    visit = set()
    #visited = [0] * (n + 1)
    #visited[1] = 1
    cnt = 0

    while q :
        v = q.popleft()
        cnt += 1
        #visited.append(v)
        visit.add(v)

        for node in array[v]:
            if node not in visit :
                visit.add(node)
                #visited[node] = 1
                q.append(node)
            
    return cnt - 1

print(bfs())
