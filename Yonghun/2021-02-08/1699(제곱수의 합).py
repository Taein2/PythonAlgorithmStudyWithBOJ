n = int(input())
D = [0] * 100001

for i in range(1, n + 1) :
    D[i] = i
    for j in range(1, i) :
        if (j * j) > i :
            break
        D[i] = min(D[i], D[i - (j * j)] + 1)

print(D[i])