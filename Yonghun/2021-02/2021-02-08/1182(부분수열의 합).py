from itertools import combinations as cb
n, s = map(int,input().split())

array = list(map(int,input().split()))
count = 0

for i in range(1, n + 1) :
    sum_value = 0
    combi = list(cb(array, i))

    for i in combi :
        sum_value += int(i)

    if sum_value == s :
        count += 1

print(count)