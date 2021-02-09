n=int(input())
a, b= 2, 1 # longer one in a
if n<=2:
    print(2 if n==2 else 1)
    exit()
for i in range(3, n+1):
    a, b= (a+b)%10007, a
print(a)