import sys; input= lambda:sys.stdin.readline().rstrip()
n= int(input())
r, g, b=0, 0, 0
for _ in range(n):
    x, y, z= map(int, input().split())
    r, g, b= x+min(g, b), y+min(r, b), z+min(r, g)
print(min(r, g, b))