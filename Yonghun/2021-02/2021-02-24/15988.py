import sys
input = sys.stdin.readline
T = int(input())
D = [0] * 10000001

D[1] = 1
D[2] = 2
D[3] = 4

for i in range(4, 10000001) :
        D[i] = (D[i-1] % 1000000009) +(D[i-2] % 1000000009) + (D[i-3] % 1000000009)

while T :
    n = int(input())
    print(D[n] % 1000000009)
    T -= 1