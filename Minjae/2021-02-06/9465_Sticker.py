import sys; input= lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n= int(input())
    u= [*map(int, input().split())]
    d= [*map(int, input().split())]
    a, b, c=0, 0, 0
    for i in range(n):
        a, b, c = max(b, c)+u[i], max(a, c)+d[i], max(a, b, c)
    print(max(a, b ,c))
