for _ in range(int(input())):
    m, n, x, y= map(int, input().split())
    x-=1
    y-=1
    if m>n:
        m, n= n, m
        x, y= y, x

    cnt=x+1
    a= x
    flag= True
    for _ in range(40000+1):
        if a==y:
            flag=False
            print(cnt)
            break
        a= (a+n-(n-m))%n
        cnt+=m

    if flag:
        print(-1)
