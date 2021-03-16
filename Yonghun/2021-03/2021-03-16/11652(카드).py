import sys
input = sys.stdin.readline
n = int(input())

result = {}

for _ in range(n) :
    tmp = int(input())
    if tmp in result :
        result[tmp] += 1
    else :
        result[tmp] = 1

print(sorted(result.items(), key = lambda x : (-x[1], x[0])))

print(result[0][0])
