# -2진수

n = int(input())

if n == 0 :
    print(0)
    exit()
ans = ""
while n :
    if n % (-2) :
        ans = '1' + ans
        n = (n // -2) + 1
    else :
        ans = '0' + ans
        n = n // -2

print(ans)