n = int(input())

D = [[0, 0, 0] for _ in range(n)]

for i in range(n) :
    temp = list(map(int,input().split()))
    if i == 0 :
        D[0] = temp
    else :
        D[i][0] = min(D[i-1][1], D[i-1][2]) + temp[0] 
        D[i][1] = min(D[i-1][0], D[i-1][2]) + temp[1]
        D[i][2] = min(D[i-1][1], D[i-1][0]) + temp[2]

print(min(D[n - 1]))