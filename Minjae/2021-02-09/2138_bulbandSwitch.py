n= int(input())
mid= (n-1)//2
# lefe
a= [int(i) for i in input()]
b= [int(i) for i in input()]
L=[0]*n
M=[0]*n

for idx, (x, y) in enumerate(zip(a,b)):
    if x!=y:
        L[idx]=1
M=L[:]
tst1=0
for i in range(mid, -1, -1):
    print(L)
    print(i)
    if L[i]==1:
        tst1+=1
        L[i]^=1
        if i-1>=0:
            L[i-1]^=1
            tst1+=1
        if i-2>=0:
            L[i-2]^=1
            tst1+=1
for i in range(mid+1, n):
    print(L)
    if L[i]==1:
        tst1+=1
        L[i]^=1
        if i+1<n:
            L[i+1]^=1
            tst1+=1
        if i+2<n:
            L[i+2]^=1
            tst1+=1

tst2=0
if M[mid]==1:
    tst2+=1
    M[mid]^=1
    if mid-1>=0:
        M[mid-1]^=1
        tst2+=1
    M[mid+1]^=1
    tst2+=1

for i in range(mid-1, -1, -1):
    print(M)
    if M[i]==1:
        tst2+=1
        M[i]^=1
        if i-1>=0:
            L[i-1]^=1
            tst2+=1
        if i-2>=0:
            M[i-2]^=1
            tst2+=1
for i in range(mid+1, n):
    print(M)
    if M[i]==1:
        tst2+=1
        M[i]^=1
        if i+1<n:
            M[i+1]^=1
        if i+2<n:
            M[i+2]^=1
print(min(tst1,tst2))





