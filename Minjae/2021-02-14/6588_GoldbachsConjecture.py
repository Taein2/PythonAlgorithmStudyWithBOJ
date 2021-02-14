net= [True]*1000001
for i in range(2,1000000//2+1):
    for j in range(2*i,1000001,i):
        net[j]=False
while True:
    n= int(input())
    if not n:
        break
    for i in range(2,n+1):
        if net[i] and net[n-i]:
            print(f'{n} = {i} + {n-i}')
            break
