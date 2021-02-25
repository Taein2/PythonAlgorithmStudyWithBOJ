import sys
input = sys.stdin.readline

t = int(input())
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
for _ in range(t):
    lst = list(map(int,input().split()))
    k = lst.pop(0)
    result = 0
    for i in range(k):
        for j in range(k):
            if i<j:
                result += gcd(lst[i],lst[j])
    print(result)