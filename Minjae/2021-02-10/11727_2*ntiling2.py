a, b= 3, 1
n= int(input())
if n==1:
    print(b)
elif n==2:
    print(a)
else:
    for i in range(3,n+1):
        a, b= (a+2*b)%10007, a
    print(a)