import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
com = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    com[a].append(b)
    com[b].append(a)

visit = [1]
result = []
while visit:
    temp = visit.pop()
    result.append(temp)
    for i in com[temp]:
        if i not in visit + result:
            visit.append(i)
print(len(result))


