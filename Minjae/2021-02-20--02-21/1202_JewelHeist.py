from heapq import heappush, heappop
# 비싼걸 작은 가방부터
n, k= map(int, input().split())
jew= []
for _ in range(n):
    w, v= map(int, input().split())
    heappush(jew, (-v, w))

bag= [[int(input()) for _ in range(k)]



def bs(k):
    lo=0
]


ans=0
while jew:
    val, wei= heappop(jew)
    if bs(wei):
        ans+=val