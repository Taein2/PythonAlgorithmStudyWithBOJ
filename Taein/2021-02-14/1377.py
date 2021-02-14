import sys
input = sys.stdin.readline

n = int(input())
arr = [(int(input()), i) for i in range(n)]
bubble = sorted(arr)
result = []
for i in range(n):
    result.append(bubble[i][1] - arr[i][1])
print(max(result) + 1)

