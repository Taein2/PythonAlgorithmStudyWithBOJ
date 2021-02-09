import sys
input = sys.stdin.readline

T = int(input())
D = [1] * 10001

for i in range(2, 10001):
    D[i] += D[i - 2] # 2를 추가해줬을 때
for i in range(3, 10001):
    D[i] += D[i - 3] # 3을 추가해줬을 때
    
for i in range(T):
    n = int(input())
    print(D[n])