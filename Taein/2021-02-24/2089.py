import sys
input = sys.stdin.readline
n = int(input())
result = []
base = 1
if n == 0:
    print(0)
else:
    while n:
        if n % 2:
            result.append(1)
            n = n - base
        else:
            result.append(0)
        base = base * -1
        n //= 2
for i in range(len(result)-1,-1,-1):
    print(result[i],end="")

