import sys,math
input = sys.stdin.readline

n,m = map(int,input().split())
square = [i**2 for i in range(2,int(math.sqrt(m)) +1)]

result = [1 for _ in range(n,m+1)]

for i in square:
    idx = (math.ceil(n/i)*i)-n
    while idx <= m - n:
        result[idx] = 0
        idx += i
count = 0
for i in range(len(result)):
    if result[i] == 1:
        count +=1
print(count)