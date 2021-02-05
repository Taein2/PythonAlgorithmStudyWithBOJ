T = int(input())
D = [0] * 101

D[1] = 1
D[2] = 2
D[3] = 4

while T :
    n = int(input())
    
    for i in range(4, n + 1) :
        D[i] = D[i-1] + D[i-2] + D[i-3]
    print(D[n])

    T -= 1