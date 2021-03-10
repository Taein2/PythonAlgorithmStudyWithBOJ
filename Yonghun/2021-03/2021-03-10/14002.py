# 가장 긴 증가하는 부분 수열 4

n = int(input())
array = list(map(int,input().split()))
D = [1] * n

for i in range(1, n) :
    for j in range(i) :
        if array[j] < array[i] :
            D[i] = max(D[i] , D[j] + 1)   

print(max(D))

result = []
order = max(D)

for i in range(n-1,-1,-1) :
    if D[i] == order :
        result.append(array[i])
        order -= 1

result.reverse()
for i in result :
    print(i, end =" ")
