n = int(input())
array = [0 for _ in range(n + 1)]
for i in range(1, n + 1) :
    array[i] = int(input())

D = [0] * (n + 1)
D[1] = array[1]
if n < 2 :
    print(D[n])
    exit()

D[2] = array[1] + array[2]
for i in range(3, n + 1) :
    D[i] = max(D[i-1], D[i-2] + array[i], D[i-3] + array[i] + array[i-1])

print(D[n])