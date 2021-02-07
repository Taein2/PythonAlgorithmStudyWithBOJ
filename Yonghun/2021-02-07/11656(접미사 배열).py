array = str(input())

result = []
for i in range(1, len(array)) :
    result.append(array[i :])

result.append(array)
result.sort()
for i in result :
    print(i)




