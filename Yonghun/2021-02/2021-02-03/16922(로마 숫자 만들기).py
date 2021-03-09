from itertools import combinations_with_replacement
n = int(input())

array = list(combinations_with_replacement(['1','5','10','50'], n))

answer = []
for i in array :
    number = 0
    for j in i :
        number += int(j)
    
    answer.append(number)
        
answer = set(answer)
print(len(answer))
    

