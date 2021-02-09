n = int(input())
array = list(map(int,input().split()))
# 3, 1, 4, 3, 2

array.sort()
# 1, 2, 3, 3, 4

sum = 0
time = []
for i in array :
    sum += i
    time.append(sum)


result = 0
for i in time : # 걸리는 시간을 모두 더해준다.
    result += i

print(result)