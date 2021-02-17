import sys
input = sys.stdin.readline
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
N, S = map(int, input().split())
location = list(map(int, input().split()))
distance = []
for i in location:
    distance.append(abs(i-S))
result = distance[0]
for idx in range(1, N):
    result = gcd(result, distance[idx])

print(result)
#list 새로만들어야함?

'''
n,s = map(int,input().split())
a = list(map(int,input().split()))
distance = []
for i in range(n):
    distance.append(abs(s-a[i]))
result = min(distance)
def solve(a,b):
    while b != 0:
        a, b = b, a % b
    return a
for i in range(1, n):
    result = solve(result, distance[i])
print(result)
'''
'''
mini = pow(10,9)
for pos in a:
    mini = min(mini, abs(s-pos))
print(mini)
'''