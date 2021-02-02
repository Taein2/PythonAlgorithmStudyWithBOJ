n= int(input())
a, b= 0, 1
for i in range(2,n+1):
    a, b= a+b, a
print(a+b)