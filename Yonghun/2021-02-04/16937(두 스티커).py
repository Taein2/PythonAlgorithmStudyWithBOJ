# 브루트포스
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())
sticker = []
ans = []

for i in range(n):
    row, col = map(int,input().split())
    sticker.append((row, col))

def solve(x, y, a, b):
    # 첫번째 스티커와 두번째 스티커 모두 안돌리는 방법
    if (x + a <= h and max(y, b) <= w) or (max(x, a) <= h and y + b <= w):
        ans.append((x * y) + (a * b))
    # 첫번째 스티커만 돌리는 경우
    elif (y + a <= h and max(x, b) <= w) or (max(y, a) <= h and x + b <= w):
        ans.append((x * y) + (a * b))
    # 두번째 스티커만 돌리는 경우
    elif (x + b <= h and max(y, a) <= w) or (max(x,b) <= h and y + a <= w):
        ans.append((x * y) + (a * b))
    # 둘 다 돌려야 하는 경우
    elif (y + b <= h and max(x, a) <= w) or (max(y, b) <= h and x + a <= w):
        ans.append((x * y) + (a * b))

for i in range(n):
    for j in range(i + 1, n):
        solve(sticker[i][0], sticker[i][1], sticker[j][0], sticker[j][1])

if ans :
    print(max(ans))
else :
    print(0)
