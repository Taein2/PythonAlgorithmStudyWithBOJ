from itertools import permutations as pm

n = int(input())
array = list(map(int,input().split()))

result = 0
pm_list = list(pm(array,n))

for pm in pm_list :
    tmp = 0
    for i in range(n - 1) :
        tmp += abs(pm[i] - pm[i + 1])
        result = max(tmp, result)

print(result)
        