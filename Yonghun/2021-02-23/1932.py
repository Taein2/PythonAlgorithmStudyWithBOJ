# 최대가 되는 경로
n = int(input())
array = []
for i in range(n) :
    array.append(list(map(int, input().split())))

for i in range(1, n) :
    for j in range(i + 1) :
        if j == 0 :
            array[i][0] = array[i-1][0] + array[i][0]
        elif i == j :
            array[i][j] = array[i-1][j-1] + array[i][j]
        else :
            array[i][j] = max(array[i-1][j-1] + array[i][j] , array[i-1][j] + array[i][j])

print(max(array[n - 1]))
