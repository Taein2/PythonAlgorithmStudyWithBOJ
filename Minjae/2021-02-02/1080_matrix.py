import sys; input= lambda: sys.stdin.readline().rstrip(); r=range
n, m= map(int, input().split())

A= [[*map(int, list(input()))] for _ in r(n)]
B= [[*map(int, list(input()))] for _ in r(n)]

def operate(y, x):
    for i in r(y, y+3):
        for j in r(x, x+3):
            A[i][j]^=1

def chk():
    same=True
    for i in r(n):
        for j in r(m):
            if A[i][j]!=B[i][j]:
                same=False
                break
    #[print(*el) for el in A]
    return same

cnt=0
for i in r(n-2): # 3 steps: -2!!
    for j in r(m-2):
        if A[i][j]!=B[i][j]:
            cnt+=1
            operate(i, j)
            if chk():
                print(cnt)
                sys.exit()
if chk():
    print(0)
else:
    print(-1)
