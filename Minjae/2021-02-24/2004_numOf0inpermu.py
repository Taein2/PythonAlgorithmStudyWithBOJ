#TLE
n, m= map(int, input().split())
cnt=0
ten1=0
two1=0
five1=0
for i in range(n,n-m-1,-1):
    while not i%10:
        ten1+=1
        i//=10
    while not i%2:
        two1+=1
        i//=2
    while not i%5:
        five1+=1
        i//=5
ten2=0
two2=0
five2=0
for i in range(1,m+1):
    while not i%10:
        ten2+=1
        i//=10
    while not i%2:
        two2+=1
        i//=2
    while not i%5:
        five2+=1
        i//=5
print(min(two1,five1)- min(two2,five2))