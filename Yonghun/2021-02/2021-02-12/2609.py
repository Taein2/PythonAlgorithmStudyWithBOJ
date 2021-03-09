import math

def lcm(a, b):
    return a * b / math.gcd(a, b)

n, m = map(int, input().split())
num1 = math.gcd(n, m)
num2 = lcm(n,m)
print(num1)
print(int(num2))