n = int(input())
T = []
P = []
D = [0] * (n + 1)

for i in range(n) :
    tmp = list(map(int,input().split()))

    T.append(tmp[0])
    P.append(tmp[1])

max_value = 0

for i in range(n) :
    max_value = max(max_value, D[i])
    if i + T[i] > n :
        continue
    D[i + T[i]] = max(max_value + P[i] , D[i + T[i]])

print(max(D))