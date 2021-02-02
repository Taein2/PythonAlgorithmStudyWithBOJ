import sys

input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())


def search(T):
    global S
    if len(S) == len(T):
        return T == S    
    if T[-1] == 'A' and search(T[:-1]):
        return True
    return T[0] == 'B' and search(T[:0:-1])


print(1 if search(T) else 0)
