e= 1000000
net= [True]*(e+1)
for i in range(2,int(e**(0.5))+1):
    if net[i]:
        for j in range(2*i, e+1, i):
            net[j]=False
prime=[]
for i in range(3,e+1):
    if net[i]:
        prime.append(i)
print(len(prime))
p= [0]*(e//2+1)
p[2]=1
for i in range(6,e+1,2): # 50만
    for el in prime: # 78497 -> 시간초과
        if el>i//2:
            break
        if net[i-el]:
            p[i//2]+=1

for _ in range(int(input())):
    n= int(input())//2
    print(p[n])

