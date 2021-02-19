import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

def solve(s):
    global t
    while t:
        if t[-1] == 'A':
            t.pop()
        elif t[-1] == 'B':
            t.pop()
            t.reverse()
        if len(s) == len(t):
            break
solve(s)
if s == t:
    print(1)
else:
    print(0)