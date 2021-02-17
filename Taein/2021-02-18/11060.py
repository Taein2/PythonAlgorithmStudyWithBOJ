import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
ans = 0
def solve(n,idx):
    global ans
    if n == 0:
        return ans
    temp = -1
    while idx != 0:
        idx -= 1
        if a[idx] + idx < n:
            continue
        temp = idx
    if temp == -1:
        return -1
    ans += 1
    return solve(temp,temp)

print(solve(n-1,n-1))


'''
now = 0
i = 0
cnt = 0
check = True
while i < n:
    if a[i] == 0:
        check = False
        break
    print(a[i])
    now = a[i]
    i = i + now
    cnt += 1
if check:
    print(cnt)
else:
    print(-1)
'''