import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush
n, k= map(int, input().split())
ls=[]
for _ in range(n):
    a, b= map(int, input().split())
    ls.append((a,b))
ls.sort(reverse=True)
bag=[]
for _ in range(k):
    bag.append(int(input()))
bag.sort()

jew=[]
ans=0
for space in bag:
    while ls and ls[-1][0]<=space:
        w, v= ls.pop()
        heappush(jew, -v)
    if jew:
        val=-heappop(jew)
        ans+=val
print(ans)

'''
7 5
2 100
11 100
12 100
10 101
10 1
10 0
10 50
1
2
10
10
10
'''