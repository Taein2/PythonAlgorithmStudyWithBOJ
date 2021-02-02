n, m = map(int,input().split())

A = [list(map(int,list(input()))) for _ in range(n)]
B = [list(map(int,list(input()))) for _ in range(n)]

def change(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            A[i][j] = 1 - A[i][j]


def check():
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return False
    return True

cnt = 0
for i in range(0, n-2):
    for j in range(0, m-2):
        if A[i][j] != B[i][j]:
            change(i,j)
            cnt += 1

if check():
    print(cnt)
else:
    print(-1)