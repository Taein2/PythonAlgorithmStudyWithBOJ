import sys
input = sys.stdin.readline

a,b,c,x,y = map(int, input().split())

money = 0

if c * 2 > a + b:
    money += a*x + b*y
else:
    if x >= y:
        money += c*2*y
        x -= y
        money += min(a * x, 2 * c * x)
    else:
        money += c*2*x
        y -= x
        money += min(b * y, 2 * c * y)
print(money)