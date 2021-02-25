import sys
input = sys.stdin.readline

n = int(input())
len = len(str(n))
count = 0
for i in range(1, len):
    count += i * (pow(10, i) - pow(10, i - 1))
count += len * (n - pow(10, len - 1) + 1)
print(count)