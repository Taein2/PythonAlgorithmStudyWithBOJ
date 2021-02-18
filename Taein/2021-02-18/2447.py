import sys
input = sys.stdin.readline


n = int(input())
star = [["*"]*n for _ in range(n)]
v = n
cnt = 0
while v != 1:
    v //= 3
    cnt += 1

for count in range(cnt):
    idx = [i for i in range(n) if (i//3 ** count) % 3 == 1]
    for i in idx:
        for j in idx:
            star[i][j] = " "

for i in star:
    print("".join(i))