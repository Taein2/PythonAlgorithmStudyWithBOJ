# 최대공약수 문제
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

N, S = map(int, input().split())
location = list(map(int, input().split()))
distance = []
for i in location:
    distance.append(abs(i- S))

result = distance[0]

for idx in range(1, N):
    result = gcd(result, distance[idx])

print(result)

# 수빈이가 서있는 위치와 각 동생들이 서있는 위치의 거리차를 구한 뒤
# 각 거리차의 약수 중 최대가 되는 수를 구하라