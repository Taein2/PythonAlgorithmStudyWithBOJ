n, m= map(int, input().split())
if n>=3 and m>=6:
    print(m-5+3)
elif n>=3:
    print(min(4,m))
elif n==2:
    if m>=7:
        print(4)
    elif m>=5:
        print(3)
    elif m>=3:
        print(2)
    else:
        print(1)
else:
    print(1)