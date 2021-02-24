def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input()) # 컴퓨터의 개수
v = int(input()) # 연결된 컴퓨터 쌍의 개수
parent = [i for i in range(n + 1)] # 먼저 모든 노드의 루트를 자신으로 지정한다.

for _ in range(v):
    a, b = map(int, input().split())
    union(parent, a, b)

answer = 0
for i in range(1, n + 1):
    if find(parent, i) == 1:
        answer += 1

print(answer-1)

# https://developmentdiary.tistory.com/443 (유니온-파인드)