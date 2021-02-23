n, k= map(int, input().split())
def fac(r):
    s=1
    for i in range(1,r+1):
        s*=i
    return s
print(fac(n)//((fac(n-k)*fac(k))))