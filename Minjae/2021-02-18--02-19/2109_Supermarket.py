from heapq import heappop, heappush
n= int(input())
mx=-1
lec= [[] for _ in range(10001)]
for _ in range(n):
    a, b= map(int, input().split())
    heappush(lec[b],-a)
ans=0
for t in range(10000,0,-1):
    tmp=[]
    for i in range(10000,t-1,-1):
        if not lec[i]:
            continue
        p= -heappop(lec[i])
        if not tmp:
            tmp=[i,p]
        else:
            if tmp[1]<p:
                heappush(lec[tmp[0]],-tmp[1])
                tmp=[i,p]
            else:
                
    if tmp:
        ans+= tmp[1]
print(ans)
