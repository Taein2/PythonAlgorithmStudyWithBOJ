import sys
input = sys.stdin.readline

n = int(input()) 
data = [tuple(map(int, input().split())) for _ in range(n)] 
charge = list(map(lambda x: x[1], data)) 

for i in range(n): 
    if i + data[i][0] > n: 
        charge[i] = 0 
    
    t = charge[i] 
    for j in range(i + data[i][0], n): 
        if t + data[j][1] > charge[j]: 
            charge[j] = t + data[j][1] 
print(max(charge))
