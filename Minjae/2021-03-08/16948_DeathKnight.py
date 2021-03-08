input()
a, b, x, y=map(int, input().split())

ans=0
dist1= abs(a-x)

if a==x and b!=y:
    if abs(b-y)%2:
        print(-1)
        exit()   
    else:    
        print(abs(b-y)//2)
        exit()
elif a!=x and b==y:
    if not abs(a-x)%4:
        print(abs(a-x)//2)
    else:
        print(-1)
    exit()

elif a==x and b==y:
    print(0)
    exit()
else:
    if b>y:
        a, x= x,a
        b, y= y,b
    cnt=0
    while a!=x:
        #print(a, b, x, y)
        b+=1
        if x<y:
            a-=2
        else:
            a+=2
        cnt+=1

        if b>y:
            print(-1)
            exit()
    #print(cnt)
    #print(a, b, x, y)
    if b>y:
        print(-1)
        exit()
    if abs(b-y)%2:
        print(-1)
        exit()
    cnt+=abs(b-y)//2
    print(cnt)