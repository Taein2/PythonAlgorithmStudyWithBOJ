n= int(input())
if n<=1:
    print(1)
    exit()
s=1
for i in range(2,n+1):
    s*=i
print(s)