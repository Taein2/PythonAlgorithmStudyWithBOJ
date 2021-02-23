n= int(input())
net=[True]*(n+1)
for i in range(2,int(n**(0.5))+1):
    if not net[i]:
        continue
    for j in range(2*i, n+1, i):
        net[j]=False

num=n
if n==1:
    exit()
for i in range(2,n+1):
    if net[i]<=num:
        while not num%i:
            print(i)
            num//=i