import sys

input = sys.stdin.readline

N = int(input())
lst = [1,5,10,50]
se = set()
def solve(x, cnt, start):
    global se
    if cnt == N:
        se.add(x)
        return
    for i in range(start,4):
        solve(x+lst[i], cnt+1, i)

solve(0,0,0)
print(len(se))