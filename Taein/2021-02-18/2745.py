import sys
input = sys.stdin.readline

n, b = map(str,input().split())
b = int(b)

result = 0

for i, j in enumerate(n):
    try:
        if int(j):
            result += int(j) * b ** (len(n)-i-1)
    except:
        result += (ord(j)-55) * b ** (len(n)-i-1)        
print(result)
#이건 뭔데 이리 어려워