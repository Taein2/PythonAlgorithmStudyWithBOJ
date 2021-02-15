n= int(input())
L= [*map(int, input().split())]
L.sort()
'''
M=L[::-1]

tst1=[]
while L:
    tst1.append(L.pop(0))
    if not L:
        break
    tst1.append(L.pop())

sum1, sum2= 0, 0
for a, b in zip(tst1,tst1[1:]):
    sum1+=abs(a-b)

tst2=[]
while M:
    tst2.append(M.pop())
    if not M:
        break
    tst2.append(M.pop(0))

for a, b in zip(tst2,tst2[1:]):
    sum2+=abs(a-b)

print(max(sum1,sum2))
'''

mx=0
chk= [False]*n
def backtrack(i, A):
    global chk
    global mx
    if i==n:
        sum=0
        for a, b in zip(A,A[1:]):
            sum+=abs(a-b)
        mx= max(sum,mx)
        return
    for j in range(n):
        if not chk[j]:
            chk[j]=True
            backtrack(i+1,A+[L[j]])
            chk[j]=False

backtrack(0,[])
print(mx)