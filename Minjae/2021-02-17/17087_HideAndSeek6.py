n, s= map(int, input().split())
L=[*map(int, input().split())]
ans=abs(L[0]-s)
def gcd(a,b) :
    if a% b == 0 :
        return b
    else :
        return gcd(b,a%b)
        
for el in L[1:]:
    ans= gcd(ans,abs(el-s))
print(ans)
