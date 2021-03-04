import sys
input = sys.stdin.readline

n,c = map(int,input().split())
x = list(int(input()) for _ in range(n))
x.sort()
start = 1
end = x[-1] - x[0]
result = 0
while end >= start:
    mid = (start+end)//2
    home = x[0]
    count = 1

    for i in range(1,n):
        if x[i] >= home + mid:
            count +=1    
            home = x[i]
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
