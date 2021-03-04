from heapq import heappush, heappop
n= int(input())
L= [int(input()) for _ in range(n)]

plus=[]
minus=[]

remain=0
zero=False
for el in L:
    if el>1:
        heappush(plus,-el)
    elif el==1:
        remain+=1
    elif el<0:
        heappush(minus,el)
    else:
        zero=True

ans=0
while len(plus)>1:
    first= heappop(plus)
    second= heappop(plus)
    ans+=first*second
if plus:
    ans=ans-heappop(plus)

while len(minus)>1:
    first= heappop(minus)
    second= heappop(minus)
    ans+=first*second
if minus and not zero:
    ans+=heappop(minus)


print(ans+remain)

#지렷닼ㅋㅋㅋㅋ