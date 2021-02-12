import sys
input = sys.stdin.readline

a, b = map(int, input().split())

A, B = a, b
while B != 0:
    A = A % B
    A, B = B, A

print(A)
print(a*b//A)
