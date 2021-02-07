for _ in range(int(input())):
    m, n, x, y= [int(i)+1 for i in input().split()]
    a, b= 1 ,1
    cnt=1
    while a<m-1 or b<n-1:
        #print(a, b)
        if a==x and b==y:
            print(cnt-1)
            exit()
        cnt+=1
        a+=1
        b+=1
        a, b= max(a%m,1), max(b%n,1)
        

    print(-1)
