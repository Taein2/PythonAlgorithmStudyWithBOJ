import sys
input = sys.stdin.readline
def solve(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

T = int(input())
for i in range(T):
    m, n, x, y = map(int, input().split())
    print(solve(m, n, x, y))
