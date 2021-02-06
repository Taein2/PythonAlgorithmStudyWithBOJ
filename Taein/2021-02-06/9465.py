import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    lst1 = [int(x) for x in input().split()]
    lst2 = [int(x) for x in input().split()]
    up = down = 0
    for i in range(N):
        up,down = max(up, down + lst1[i]),max(down, up + lst2[i])
        print(up)
        print(down)
    print(max(up, down))