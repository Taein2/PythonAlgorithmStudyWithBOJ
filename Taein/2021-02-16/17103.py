import sys
input = sys.stdin.readline

r = 1000001
check = [True for _ in range(r)]

for i in range(2,int(r**0.6)):
    if check[i]==True:
        for j in range(i*2, r, i): 
            if check[j] == True:
                check[j] = False

t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for j in range(3,(n//2)+1):
        if check[j] and check[n-j]:
            count +=1
    print(count)
