# WA
n, k= map(int, input().split())

for j in range(2,n+1):
    for i in range(1,j+1):
        if i*(j-i)==k:
            print('B'*(n-j)+'A'*i+'B'*(j-i))
            exit()
print(-1)