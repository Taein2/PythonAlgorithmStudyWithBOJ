# 타일 채우기

# 짝수만 가능하네
n = int(input())

D = [0 for _ in range(31)]
D[0] = 1
D[2] = 3
for i in range(4, 31,2) :
    D[i] = D[i-2] * 3 
    for j in range(4, i + 1, 2) :
        D[i] += D[i-j] * 2

if n % 2 == 1 :
    print(0)
else :
    print(D[n])