from collections import deque
n = int(input())
array = list(map(int,input().split()))

D = [-1] * n

q = deque()
q.append(0)
D[0] = 0
while q :
    now = q.popleft()
    value = array[now]
    for i in range(value, 0, -1) :
        if now + i < n and D[now + i] == -1 :
            D[now + i] = D[now] + 1
            q.append(now + i)

print(D[-1])
