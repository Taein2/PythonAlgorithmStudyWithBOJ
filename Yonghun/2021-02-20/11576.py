import math
A, B = map(int,input().split())
m = int(input())

array = list(map(int,input().split()))
answer = []
tmp = 0
for i in range(m) :
    tmp += int(array[i] * math.pow(A, m - i - 1))


while tmp != 0 :
    answer.append(str(tmp % B))
    tmp = tmp // B

print(" ".join(answer[::-1]))    
print(answer)