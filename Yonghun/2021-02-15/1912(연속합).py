n = int(input())
array = list(map(int,input().split()))
D = [0] * n

D[0] = array[0]

for i in range(1, n) :
    D[i] = max(array[i], D[i - 1] + array[i])

print(D)
print(max(D))