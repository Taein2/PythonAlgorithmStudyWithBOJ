n= int(input())
z, l, r= 1, 1, 1
for _ in range(1,n):
    z, l, r= (z+l+r)%9901, (z+r)%9901, (z+l)%9901
print((z+l+r)%9901)