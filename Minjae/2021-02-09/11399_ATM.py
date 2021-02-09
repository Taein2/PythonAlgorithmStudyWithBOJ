n= int(input())
L= sorted([*map(int, input().split())])
s=0
for i in range(n):
    s+=L[i]*(n-i)
print(s)
