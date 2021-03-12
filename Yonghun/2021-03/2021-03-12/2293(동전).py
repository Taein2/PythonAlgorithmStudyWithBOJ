n, k = map(int,input().split()) 
coin = []
for _ in range(n) :
    coin.append(int(input()))

D = [0] * 10001

D[0] = 1

for i in coin :
    for j in range(i, k + 1) :
        D[j] += D[j - i]


print(D[k])