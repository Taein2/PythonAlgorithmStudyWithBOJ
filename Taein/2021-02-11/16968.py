import sys
input = sys.stdin.readline

n = input().rstrip()

result = 0
if n[0] == 'c':
    result += 26
else :
    result += 10
for i in range(1,len(n)):
    if n[i] == 'c':
        if n[i-1] == 'c':
            result *= 25
        else:
            result *= 26
    elif n[i] == 'd':
        if n[i-1] == 'd':
            result *= 9
        else:
            result *= 10
print(result)