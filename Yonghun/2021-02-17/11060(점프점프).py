import sys
input = sys.stdin.readline
INF = 1e9

n = int(input())
array = list(map(int,input().split()))
D = [INF] * n
D[0] = 0

for i in range(n):
    for j in range(1, array[i] + 1):
        if i + j < n:
            D[i + j] = min(D[i + j], D[i] + 1)

if D[n-1] == INF:
    print(-1)
else:
    print(D[n-1])
