import math
min, max = map(int,input().split())

answer = [1] * (max - min + 1)


Square = []

i = 2
while i**2 <= max :
    Square.append(i**2)
    i += 1

for num in Square:
    j = math.ceil(min/num)
    while num*j <= max :
        answer[num*j-min] = 0
        j += 1

print(answer.count(1))

