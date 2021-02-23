A, B= map(int, input().split())
n= int(input())
L=[*map(int, input().split())]

deci=0
for idx, el in enumerate(reversed(L)):
    deci+=(A**idx)*el
ans=[]
while deci>=B:
    ans.append(deci%B)
    deci//=B
ans.append(deci)
print(*reversed(ans))
