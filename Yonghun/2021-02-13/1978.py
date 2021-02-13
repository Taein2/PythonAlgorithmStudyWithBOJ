N = int(input())

a = list(map(int,input().split()))
# [1,3,5,7]
res = 0


for i in a :
    count = 0
    for j in range(1, i + 1) :
        if i % j == 0 :
            count += 1
    if count == 2:
        res += 1        


print(res)     