# MLE
from heapq import heappush, heappop
from collections import deque
# 비싼걸 작은 가방부터
n, k= map(int, input().split())
jew= []
for _ in range(n):
    w, v= map(int, input().split())
    heappush(jew, (-v, -w)) # 가치 큰 순으로. 무거운순으로

bag= [int(input()) for _ in range(k)]
bag.sort() # 작은 크기 가방순으로 
# bisect
chk= [i for i in range(k)]


def bs(weight):

    lo=0
    hi= k-1
    answer=-1
    while lo<=hi:
        m=(lo+hi)//2
        if bag[m]>=weight: #답이 될 수 있다
            answer=m
            hi=m-1
        else:
            lo=m+1
    return answer

ans=0
unfilled=k # 가방의 개수. 하나 채울때마다 -1해준다.
pointing={}
for i in range(k):
    pointing[i]={i}
#print(bag)
#print(chk)
while unfilled and jew:

    val, wei= heappop(jew)
    val=-val # 큰순으로 가치 가져왔음
    wei=-wei
    #print(val,wei)
    
    loc= bs(wei)# wei넣을 수 있는 가장 작은 가방의 인덱스 가져옴
    if loc==-1: # 가방이 무게보다 작으면 못넣고 지나감
        continue
    if chk[loc]>=0: # 빈자리 있으면 집어넣음

        if loc+1==k:
            chk[loc]=-1
            continue

        ans+=val
        unfilled-=1
        if chk[loc]+1==k:
            chk[loc]=-1
            for v in pointing[loc]:
                #print(v)
                chk[v]=-1
            pointing[loc]={}
            continue

        new=chk[chk[loc]+1]
        #print('loc',loc)
        #print('new:',new)
         # 다음 빈좌표로 바꿔줌
        pointing[new].add(loc)
        #print(chk)
        #print(chk[loc],'인 애들',pointing[chk[loc]])
        for v in pointing[chk[loc]]:
            #print(v)
            chk[v]=new
            pointing[new].add(v)
        pointing[loc]={}
    #print(chk)

    #print('ans',ans)
print(ans)

#print(bs(11))

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


5 5
9 5
4 4
1 3
11 2
1 1
2
3
4
10
10
'''

# 1 2 3 4 10