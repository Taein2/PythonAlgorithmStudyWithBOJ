p1,p2,p3,x1,x2,x3 = map(int,input().split())

n = 1
for i in range(1, (p1 * p2 * p3) + 1) : # 최소공배수
    if i % p1 == x1 and i % p2 == x2 and i % p3 == x3 :
        print(i)
        exit()
    
print(-1)