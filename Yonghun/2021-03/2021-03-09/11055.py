# 가장 큰 증가 부분 수열

n = int(input())
array = list(map(int,input().split()))

D = [i for i in array] # D 배열을 array 값으로 초기화시켜야 한다.
#print(D)

D[0] = array[0]
for i in range(1, n) :
    for j in range(i) :
        if array[j] < array[i] :
            D[i] = max(D[i], D[j] + array[i])

print(max(D))
