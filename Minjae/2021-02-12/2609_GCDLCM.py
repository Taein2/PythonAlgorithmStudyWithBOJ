a, b= map(int, input().split())
def gcd(a, b):
    if not a*b:
        return a+b
    if a>b:
        return gcd(a%b, b)
    else:
        return gcd(a,b%a)
def lcm(a, b, GCD):
    return GCD*(a//GCD)*(b//GCD)

c= gcd(a,b)
print(c, lcm(a,b,c), sep='\n')
