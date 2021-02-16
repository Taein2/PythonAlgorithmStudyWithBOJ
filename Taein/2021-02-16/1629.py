import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
print(pow(a,b,c))
'''
def solve(a,b):
    if b == 1:
        return a%c
    else:
        temp = solve(a,b//2)
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c
print(solve(a,b))
'''