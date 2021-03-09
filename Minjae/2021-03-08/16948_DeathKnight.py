n= int(input())
a, b, x, y=map(int, input().split())
if a>=n or b>=n or x>=n or y>=n or a<0 or b<0 or x<0 or y<0:
    print(-1)
    exit()

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
    if abs(a-x)%2:
        print(-1)
        exit()

    while a!=x and b!=y:
        b+=1
        if a>x:
            a-=2
        else:
            a+=2
        cnt+=1

    if b!=y and a==x:
        if abs(b-y)%2:
            print(-1)
            exit()   
        cnt+=abs(b-y)//2
        print(cnt)
    
    elif a!=x and b==y:
        if abs(a-x)%4:
            print(-1)
            exit()   
        cnt+=abs(a-x)//2
        print(cnt)
    else:
        print(cnt)