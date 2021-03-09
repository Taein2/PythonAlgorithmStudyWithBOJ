
n = int(input())
D = [0] * 100001

D[0] = 1
D[1] = 3
D[2] = 7
for i in range(3, n + 1) :
    D[i] = (D[i - 1]*2 + D[i - 2]) % 9901

print(D[n])