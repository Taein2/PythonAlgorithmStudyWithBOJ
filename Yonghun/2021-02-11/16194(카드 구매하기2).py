n = int(input())
D = [False] * (n + 1)
array = [0] + list(map(int, input().split()))

D[1] = array[1] # 1번 카드 1번 쓰면 된다.
D[2] = min(array[2], array[1] * 2) # 1번 카드 2개 쓰거나, 2번 카드 하나 쓰기.

for i in range(3, n + 1):
    for j in range(1, i + 1):
        if D[i] == False :
            D[i] = D[i-j] + array[j]
        else :
            D[i] = min(D[i], D[i-j] + array[j])

print(D[n])

