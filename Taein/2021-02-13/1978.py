import sys
input = sys.stdin.readline

n = int(input())
sosu = list(map(int,input().split()))
result = 0
for i in range(n):
    count = 0
    for j in range(1,sosu[i]+1):
        if sosu[i] % j == 0:
            count +=1
    if count == 2:
        result += 1
print(result)