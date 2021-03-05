import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))

start = 1
end = max(lst)

while start <= end:
    mid = (start+end)//2

    count = 0
    for i in lst:
        if i >= mid:
            count += i - mid
    if count >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)