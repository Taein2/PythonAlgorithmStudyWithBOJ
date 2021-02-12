a, b, c, x, y= map(int, input().split())

if a+b>2*c:
    ans= 2*c*min(x, y)
    if x>y:
        if a>c*2:
            ans+=2*c*(x-y)
        else:
            ans+=a*(x-y)
    elif x<y:
        if b>c*2:
            ans+=2*c*(y-x)
        else:
            ans+=b*(y-x)
else:
    ans= a*x+ b*y
print(ans)