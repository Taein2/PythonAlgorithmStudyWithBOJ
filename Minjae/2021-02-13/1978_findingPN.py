net= [True]*(1001)
net[1]=False
for i in range(2,501):
    for j in range(i*2, 1001,i):
        net[j]=False
cnt=0
n= int(input())
L= [*map(int, input().split())]
for el in L:
    if net[el]:
        cnt+=1
print(cnt)
