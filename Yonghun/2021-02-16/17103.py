tc = int(input())
T = 1000001
check = [True for _ in range(T)]

for i in range(2, int(T**0.5)):
    if check[i] == True :
        for j in range(i+i, T, i) : 
            if check[j] == True :
                check[j] = False            


for i in range(tc) :                           
    n = int(input())
    count = 0
    for i in range(2, n//2 + 1): # 중복을 제거하기 위해 n//2까지만 탐색
        if check[i] and check[n-i] :
            count += 1
                
    print(count)