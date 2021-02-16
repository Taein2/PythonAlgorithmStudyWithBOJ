from itertools import permutations as pm
a, b = map(int,input().split())

length = len(str(a))
c = list(pm(str(a), length))
array = []
for i in c :
    array.append("".join(i))

answer = -1
for i in array:
    first = i[0]
    i = int(i)
    if b >= i and first != '0':
        answer = max(answer, i)
print(answer)
