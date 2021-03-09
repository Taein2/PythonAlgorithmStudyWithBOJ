n = input()
result = ''

if '0' not in n :
    print(-1)

else :
    Sum = 0
    for i in n :
        Sum += int(i) 

    if Sum % 3 != 0 :
        print(-1)
    else :
        n = sorted(n, reverse = True)
        for i in n :
            result += i

print(result)
