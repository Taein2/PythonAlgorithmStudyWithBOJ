import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

count = 0
for i in range(N-1,-1,-1):
  if K >= coin[i] :
    count += K//coin[i]
    K = K % coin[i]
print(count) 
