import sys
input = sys.stdin.readline

T = 1000001
check = [True for _ in range(T)]

for i in range(2, int(T**0.5)):
    if check[i] == True :
        for j in range(i+i, T, i) : 
            if check[j] == True :
                check[j] = False            

while 1:                              
    n = int(input())
    if n == 0 : 
        break

    for i in range(3, T):
        if check[i] == True:
            if check[n - i] == True :
                print("%d = %d + %d"%(n , i , n - i))
                break